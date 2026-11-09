"""
Integration tests for FastAPI REST endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from backend.main import app

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

def test_api_products_list(client):
    res = client.get("/api/products")
    assert res.status_code == 200
    data = res.json()
    assert data["total"] >= 50
    assert len(data["products"]) > 0

def test_api_products_filter_category(client):
    res = client.get("/api/products?category=Mobiles")
    assert res.status_code == 200
    products = res.json()["products"]
    assert len(products) > 0
    for p in products:
        assert p["category"] == "Mobiles"

def test_api_product_detail(client):
    res = client.get("/api/products/MOB-APPL-IP15")
    assert res.status_code == 200
    data = res.json()
    assert data["id"] == "MOB-APPL-IP15"
    assert "competitors" in data
    assert "reviews" in data

def test_api_categories(client):
    res = client.get("/api/categories")
    assert res.status_code == 200
    data = res.json()
    assert "Mobiles" in data["categories"]
    assert "Apple" in data["brands"]

def test_api_compare(client):
    res = client.get("/api/compare?ids=MOB-APPL-IP15,MOB-SAMS-S24")
    assert res.status_code == 200
    data = res.json()
    assert len(data["products"]) == 2
    assert "comparison_matrix" in data

def test_api_chat(client):
    res = client.post("/api/chat", json={
        "query": "Best gaming laptop under 150000",
        "mode": "shopping"
    })
    assert res.status_code == 200
    data = res.json()
    assert "response" in data
    assert "agent_trace" in data
    assert len(data["products"]) > 0

def test_api_bi_overview(client):
    res = client.get("/api/bi/overview")
    assert res.status_code == 200
    data = res.json()
    assert data["total_products"] >= 50
    assert data["monthly_gmv_inr"] > 0

def test_api_bi_pricing(client):
    res = client.get("/api/bi/pricing")
    assert res.status_code == 200
    data = res.json()
    assert "benchmarks" in data
    assert "sample_elasticity" in data

def test_api_bi_sentiment(client):
    res = client.get("/api/bi/sentiment")
    assert res.status_code == 200
    data = res.json()
    assert "aspect_breakdown" in data

def test_api_bi_trends(client):
    res = client.get("/api/bi/trends")
    assert res.status_code == 200
    data = res.json()
    assert "category_trends" in data

def test_api_bi_simulate(client):
    res = client.post("/api/bi/simulate-price", json={
        "product_id": "MOB-APPL-IP15",
        "discount_pct_delta": 3.0
    })
    assert res.status_code == 200
    data = res.json()
    assert data["product_id"] == "MOB-APPL-IP15"
    assert "simulated_profit" in data
