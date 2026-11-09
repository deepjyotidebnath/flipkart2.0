"""
Unit and integration tests for ML Analytics Engine.
"""

import pytest
from backend.engine.analytics import AnalyticsEngine

@pytest.fixture(scope="module")
def analytics():
    return AnalyticsEngine()

def test_executive_overview(analytics):
    overview = analytics.compute_executive_overview()
    assert overview["total_products"] >= 50
    assert overview["monthly_gmv_inr"] > 100000000
    assert overview["avg_margin_pct"] > 0
    assert overview["price_competitiveness_index"] > 50
    assert 0.0 <= overview["overall_sentiment_score"] <= 1.0

def test_competitor_benchmarks(analytics):
    benchmarks = analytics.compute_competitor_benchmarks()
    assert len(benchmarks) > 0
    first = benchmarks[0]
    assert "flipkart_price" in first
    assert "lowest_competitor_price" in first
    assert "status" in first
    assert first["status"] in ["Best Price", "Parity", "Overpriced"]

def test_price_elasticity_simulation(analytics):
    # Test valid product
    sim = analytics.simulate_price_elasticity("MOB-APPL-IP15", discount_pct_delta=5.0)
    assert sim["product_id"] == "MOB-APPL-IP15"
    assert sim["simulated_price"] < sim["current_price"]
    assert sim["simulated_units"] > sim["current_units"]
    assert "optimal_recommendation" in sim
    assert len(sim["elasticity_curve"]) > 0

def test_sentiment_breakdown(analytics):
    sent = analytics.compute_sentiment_breakdown()
    assert "aspect_breakdown" in sent
    assert "category_sentiment" in sent
    assert len(sent["aspect_breakdown"]) > 0

def test_market_trends(analytics):
    trends = analytics.compute_market_trends()
    assert "category_trends" in trends
    assert "inventory_risk_alerts" in trends
    assert len(trends["category_trends"]) > 0
