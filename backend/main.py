"""
FastAPI Application serving REST endpoints for:
- LangGraph Multi-Agent Chat (/api/chat)
- Product Catalog, Filters, and Details (/api/products)
- Side-by-Side Product Comparison (/api/compare)
- E-Commerce Business Intelligence APIs:
  - Executive Overview (/api/bi/overview)
  - Competitor Benchmarks & Elasticity (/api/bi/pricing)
  - Aspect Sentiment Mining (/api/bi/sentiment)
  - Demand Trends & Stock-Out Risks (/api/bi/trends)
  - Interactive Discount Simulator (/api/bi/simulate-price)
- Static Frontend Dashboard Serving
"""

import os
import json
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from backend.data.db import get_connection
from backend.engine.rag import rag_engine
from backend.engine.analytics import analytics_engine
from backend.agents.graph import multi_agent_app

app = FastAPI(
    title="Flipkart Intelligence Agent API",
    description="Multi-Agent E-Commerce Intelligence & AI Shopping Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- Request Models -----------------
class ChatRequest(BaseModel):
    query: str
    mode: str = Field(default="shopping", description="'shopping' or 'business'")
    session_id: Optional[str] = "session-default"
    history: Optional[List[Dict[str, str]]] = []

class PriceSimulationRequest(BaseModel):
    product_id: str
    discount_pct_delta: float = 0.0

# ----------------- Chat / Multi-Agent Endpoints -----------------
@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    """
    Executes multi-agent LangGraph workflow.
    Returns agent execution trace, final markdown answer, product recommendations, and suggested questions.
    """
    initial_state = {
        "messages": req.history or [],
        "user_query": req.query,
        "session_id": req.session_id or "session-default",
        "mode": req.mode,
        "intent": "",
        "entities": {},
        "retrieved_products": [],
        "retrieved_reviews": [],
        "comparison_data": None,
        "analytics_data": None,
        "agent_trace": [],
        "final_response": "",
        "recommended_products": [],
        "quick_suggestions": []
    }

    try:
        result_state = multi_agent_app.invoke(initial_state)
        return {
            "query": req.query,
            "mode": req.mode,
            "intent": result_state.get("intent"),
            "response": result_state.get("final_response"),
            "agent_trace": result_state.get("agent_trace", []),
            "products": result_state.get("recommended_products", []),
            "comparison": result_state.get("comparison_data"),
            "analytics": result_state.get("analytics_data"),
            "suggestions": result_state.get("quick_suggestions", [])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------------- Product Catalog Endpoints -----------------
@app.get("/api/products")
async def list_products(
    category: Optional[str] = None,
    brand: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    sort_by: Optional[str] = "popular", # "price_asc", "price_desc", "rating", "discount"
    search: Optional[str] = None,
    limit: int = 50
):
    if search:
        # Use hybrid RAG search
        results = rag_engine.search(
            query=search,
            category=category,
            brand=brand,
            min_price=min_price,
            max_price=max_price,
            top_k=limit
        )
        return {"total": len(results), "products": results}

    conn = get_connection()
    cur = conn.cursor()
    query = "SELECT * FROM products WHERE 1=1"
    params = []

    if category:
        query += " AND (category = ? OR sub_category = ?)"
        params.extend([category, category])
    if brand:
        query += " AND brand = ?"
        params.append(brand)
    if min_price is not None:
        query += " AND price >= ?"
        params.append(min_price)
    if max_price is not None:
        query += " AND price <= ?"
        params.append(max_price)

    if sort_by == "price_asc":
        query += " ORDER BY price ASC"
    elif sort_by == "price_desc":
        query += " ORDER BY price DESC"
    elif sort_by == "rating":
        query += " ORDER BY rating DESC"
    elif sort_by == "discount":
        query += " ORDER BY discount_pct DESC"
    else:
        query += " ORDER BY monthly_sales_units DESC"

    query += " LIMIT ?"
    params.append(limit)

    cur.execute(query, params)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()

    for r in rows:
        r["specs"] = json.loads(r.get("specs_json", "{}"))
        r["features"] = json.loads(r.get("features_json", "[]"))

    return {"total": len(rows), "products": rows}


@app.get("/api/products/{product_id}")
async def get_product_detail(product_id: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = cur.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")

    p = dict(row)
    p["specs"] = json.loads(p.get("specs_json", "{}"))
    p["features"] = json.loads(p.get("features_json", "[]"))

    # Competitors
    cur.execute("SELECT * FROM competitor_prices WHERE product_id = ?", (product_id,))
    p["competitors"] = [dict(c) for c in cur.fetchall()]

    # Reviews
    cur.execute("SELECT * FROM reviews WHERE product_id = ? ORDER BY helpful_count DESC", (product_id,))
    revs = [dict(r) for r in cur.fetchall()]
    for r in revs:
        r["aspects"] = json.loads(r.get("aspects_json", "{}"))
    p["reviews"] = revs

    conn.close()
    return p


@app.get("/api/categories")
async def get_categories():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT category FROM products")
    cats = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT DISTINCT brand FROM products ORDER BY brand")
    brands = [row[0] for row in cur.fetchall()]
    conn.close()
    return {"categories": cats, "brands": brands}


@app.get("/api/compare")
async def compare_products(ids: str):
    """
    Compare multiple products given comma-separated product IDs (e.g. ?ids=MOB-APPL-IP15,MOB-SAMS-S24)
    """
    id_list = [i.strip() for i in ids.split(",") if i.strip()]
    if len(id_list) < 2:
        raise HTTPException(status_code=400, detail="Provide at least two product IDs to compare.")

    conn = get_connection()
    cur = conn.cursor()
    placeholders = ",".join(["?"] * len(id_list))
    cur.execute(f"SELECT * FROM products WHERE id IN ({placeholders})", id_list)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()

    if len(rows) < 2:
        raise HTTPException(status_code=404, detail="Could not find specified products to compare.")

    for r in rows:
        r["specs"] = json.loads(r.get("specs_json", "{}"))
        r["features"] = json.loads(r.get("features_json", "[]"))

    # Collect all specs keys
    all_keys = set()
    for r in rows:
        all_keys.update(r["specs"].keys())

    comparison_table = []
    for k in sorted(all_keys):
        row = {"spec_name": k}
        for r in rows:
            row[r["id"]] = r["specs"].get(k, "—")
        comparison_table.append(row)

    return {
        "products": rows,
        "spec_keys": sorted(all_keys),
        "comparison_matrix": comparison_table
    }

# ----------------- Business Intelligence Endpoints -----------------
@app.get("/api/bi/overview")
async def bi_overview():
    kpis = analytics_engine.compute_executive_overview()
    return kpis

@app.get("/api/bi/pricing")
async def bi_pricing():
    benchmarks = analytics_engine.compute_competitor_benchmarks()
    # Also attach default elasticity for the top product
    elasticity = analytics_engine.simulate_price_elasticity("MOB-APPL-IP15", 0.0)
    return {
        "benchmarks": benchmarks,
        "sample_elasticity": elasticity
    }

@app.get("/api/bi/sentiment")
async def bi_sentiment():
    return analytics_engine.compute_sentiment_breakdown()

@app.get("/api/bi/trends")
async def bi_trends():
    return analytics_engine.compute_market_trends()

@app.post("/api/bi/simulate-price")
async def bi_simulate(req: PriceSimulationRequest):
    return analytics_engine.simulate_price_elasticity(req.product_id, req.discount_pct_delta)

# ----------------- Static Frontend Mount -----------------
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(FRONTEND_DIR):
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
