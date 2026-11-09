"""
Hybrid RAG Engine (TF-IDF Vector Space + BM25-style Keyword Matching + Structured Metadata Filters).
Indexes product specs, descriptions, features, and customer reviews to provide grounded e-commerce context.
"""

import json
import math
import re
from typing import List, Dict, Any, Optional
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from backend.data.db import get_connection

class HybridRAGEngine:
    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path
        self.documents = []
        self.doc_metadata = []
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            stop_words='english',
            max_features=5000
        )
        self.tfidf_matrix = None
        self.indexed = False
        self.build_index()

    def build_index(self):
        conn = get_connection(self.db_path) if self.db_path else get_connection()
        cur = conn.cursor()

        # 1. Fetch Products
        cur.execute("SELECT * FROM products")
        products = [dict(row) for row in cur.fetchall()]

        # 2. Fetch Reviews grouped by product
        cur.execute("SELECT * FROM reviews")
        reviews = [dict(row) for row in cur.fetchall()]
        reviews_by_pid = {}
        for r in reviews:
            pid = r["product_id"]
            if pid not in reviews_by_pid:
                reviews_by_pid[pid] = []
            reviews_by_pid[pid].append(r)

        # 3. Fetch Competitors
        cur.execute("SELECT * FROM competitor_prices")
        competitors = [dict(row) for row in cur.fetchall()]
        comp_by_pid = {}
        for c in competitors:
            pid = c["product_id"]
            if pid not in comp_by_pid:
                comp_by_pid[pid] = []
            comp_by_pid[pid].append(c)

        conn.close()

        docs = []
        meta = []

        for p in products:
            pid = p["id"]
            specs = json.loads(p.get("specs_json", "{}"))
            features = json.loads(p.get("features_json", "[]"))
            p_reviews = reviews_by_pid.get(pid, [])
            p_comp = comp_by_pid.get(pid, [])

            review_summary_parts = [
                f"{r.get('title', '')}: {r.get('review_text', '')}" for r in p_reviews
            ]
            review_text_blob = " | ".join(review_summary_parts)

            specs_blob = " ".join([f"{k}: {v}" for k, v in specs.items()])
            features_blob = ", ".join(features)

            content = (
                f"{p['title']} brand {p['brand']} category {p['category']} {p.get('sub_category', '')}. "
                f"Price ₹{p['price']} (Original ₹{p['original_price']}, discount {p['discount_pct']}%). "
                f"Rating: {p['rating']} stars ({p['rating_count']} reviews). "
                f"Specs: {specs_blob}. "
                f"Highlights: {features_blob}. "
                f"Description: {p['description']}. "
                f"Customer Opinions: {review_text_blob}"
            )

            docs.append(content)
            meta.append({
                "type": "product",
                "id": pid,
                "title": p["title"],
                "brand": p["brand"],
                "category": p["category"],
                "sub_category": p.get("sub_category", ""),
                "price": float(p["price"]),
                "original_price": float(p["original_price"]),
                "discount_pct": float(p["discount_pct"]),
                "rating": float(p["rating"]),
                "rating_count": int(p["rating_count"]),
                "stock": int(p["stock"]),
                "image_url": p["image_url"],
                "specs": specs,
                "features": features,
                "description": p["description"],
                "reviews_count": len(p_reviews),
                "reviews": p_reviews,
                "competitors": p_comp,
                "raw_content": content
            })

            # Also create granular review chunks for deep customer sentiment RAG
            for rev in p_reviews:
                rev_aspects = json.loads(rev.get("aspects_json", "{}"))
                rev_content = (
                    f"Product: {p['title']} ({p['brand']}). Review by {rev['author']} "
                    f"Rating {rev['rating']}/5: {rev.get('title', '')} - {rev['review_text']}. "
                    f"Key Aspects: {list(rev_aspects.keys())}"
                )
                docs.append(rev_content)
                meta.append({
                    "type": "review",
                    "product_id": pid,
                    "product_title": p["title"],
                    "rating": float(rev["rating"]),
                    "author": rev["author"],
                    "review_text": rev["review_text"],
                    "aspects": rev_aspects,
                    "raw_content": rev_content
                })

        self.documents = docs
        self.doc_metadata = meta
        if docs:
            self.tfidf_matrix = self.vectorizer.fit_transform(docs)
        self.indexed = True

    def _bm25_score(self, query_tokens: List[str], doc_tokens: List[str], avgdl: float, k1=1.5, b=0.75) -> float:
        score = 0.0
        doc_len = len(doc_tokens)
        token_set = set(doc_tokens)
        for q in query_tokens:
            if q in token_set:
                freq = doc_tokens.count(q)
                numerator = freq * (k1 + 1)
                denominator = freq + k1 * (1 - b + b * (doc_len / (avgdl + 1e-5)))
                score += (numerator / (denominator + 1e-5))
        return score

    def search(
        self,
        query: str,
        category: Optional[str] = None,
        max_price: Optional[float] = None,
        min_price: Optional[float] = None,
        min_rating: Optional[float] = None,
        brand: Optional[str] = None,
        doc_type: str = "product",
        top_k: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Executes hybrid retrieval:
        1. Cosine similarity on TF-IDF representation
        2. Exact BM25 token matching
        3. Hard metadata filters
        """
        if not self.indexed or not self.documents:
            return []

        # Vector score
        q_vec = self.vectorizer.transform([query])
        dense_vec = q_vec.toarray()[0]
        # Avoid division by zero
        norm_q = np.linalg.norm(dense_vec)
        if norm_q > 0:
            dense_vec = dense_vec / norm_q

        tfidf_scores = (self.tfidf_matrix.dot(dense_vec)).flatten()

        query_tokens = [w.lower() for w in re.findall(r'\b[a-zA-Z0-9\-\+]+\b', query)]
        avgdl = np.mean([len(d.split()) for d in self.documents]) if self.documents else 1.0

        results = []
        for i, m in enumerate(self.doc_metadata):
            # Check type filter
            if doc_type and m.get("type") != doc_type:
                continue

            # Check metadata filters for products
            if m.get("type") == "product":
                if category and category.lower() not in m["category"].lower() and category.lower() not in m["sub_category"].lower():
                    continue
                if brand and brand.lower() != m["brand"].lower():
                    continue
                if max_price is not None and m["price"] > max_price:
                    continue
                if min_price is not None and m["price"] < min_price:
                    continue
                if min_rating is not None and m["rating"] < min_rating:
                    continue

            # Hybrid score calculation
            vec_s = float(tfidf_scores[i])
            doc_toks = [w.lower() for w in re.findall(r'\b[a-zA-Z0-9\-\+]+\b', self.documents[i])]
            bm25_s = self._bm25_score(query_tokens, doc_toks, avgdl)

            # Combined score: 60% TF-IDF cosine + 40% BM25 keyword relevance
            combined_score = 0.6 * vec_s + 0.4 * (bm25_s / (1.0 + bm25_s))

            # Query token bonus for exact product title match
            title_lower = m.get("title", m.get("product_title", "")).lower()
            if any(q in title_lower for q in query_tokens if len(q) > 3):
                combined_score += 0.25

            item = dict(m)
            item["hybrid_score"] = round(combined_score, 4)
            results.append(item)

        results.sort(key=lambda x: x["hybrid_score"], reverse=True)
        return results[:top_k]

# Global singleton instance
rag_engine = HybridRAGEngine()
