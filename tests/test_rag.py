"""
Unit and integration tests for Hybrid RAG Engine.
"""

import pytest
from backend.engine.rag import HybridRAGEngine

@pytest.fixture(scope="module")
def rag():
    return HybridRAGEngine()

def test_rag_build_index(rag):
    assert rag.indexed is True
    assert len(rag.documents) > 0
    assert rag.tfidf_matrix is not None

def test_rag_search_relevance(rag):
    results = rag.search("Apple iPhone 15", top_k=3)
    assert len(results) > 0
    top = results[0]
    assert "Apple" in top["brand"] or "iPhone" in top["title"]

def test_rag_category_filter(rag):
    results = rag.search("gaming laptop", category="Laptops", top_k=5)
    assert len(results) > 0
    for r in results:
        assert r["category"] == "Laptops"

def test_rag_budget_filter(rag):
    results = rag.search("smartphone", category="Mobiles", max_price=30000.0, top_k=5)
    assert len(results) > 0
    for r in results:
        assert r["price"] <= 30000.0

def test_rag_review_search(rag):
    results = rag.search("battery life fast charging", doc_type="review", top_k=3)
    assert len(results) > 0
    assert results[0]["type"] == "review"
