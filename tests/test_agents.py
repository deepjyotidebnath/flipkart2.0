"""
Integration tests for LangGraph multi-agent orchestration.
"""

import pytest
from backend.agents.graph import multi_agent_app

def create_initial_state(query: str, mode: str = "shopping"):
    return {
        "messages": [],
        "user_query": query,
        "session_id": "test-session",
        "mode": mode,
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

def test_shopping_discovery_agent():
    state = create_initial_state("Best smartphone under 30000", mode="shopping")
    out = multi_agent_app.invoke(state)
    assert out["intent"] == "discovery"
    assert len(out["recommended_products"]) > 0
    assert "RouterAgent" in [t["agent"] for t in out["agent_trace"]]
    assert "DiscoveryAgent" in [t["agent"] for t in out["agent_trace"]]
    assert "SynthesizerNode" in [t["agent"] for t in out["agent_trace"]]
    assert len(out["final_response"]) > 20

def test_shopping_comparison_agent():
    state = create_initial_state("Compare iPhone 15 vs OnePlus 12R", mode="shopping")
    out = multi_agent_app.invoke(state)
    assert out["intent"] == "compare"
    assert "ComparisonAgent" in [t["agent"] for t in out["agent_trace"]]
    assert out["comparison_data"] is not None
    assert "product_a" in out["comparison_data"]
    assert "specs_matrix" in out["comparison_data"]

def test_shopping_evaluation_agent():
    state = create_initial_state("Is Sony WH-1000XM5 worth buying?", mode="shopping")
    out = multi_agent_app.invoke(state)
    assert out["intent"] == "evaluate"
    assert "EvaluationAgent" in [t["agent"] for t in out["agent_trace"]]
    assert out["analytics_data"] is not None

def test_business_pricing_agent():
    state = create_initial_state("Show pricing elasticity and competitor benchmarks for iPhone 15", mode="business")
    out = multi_agent_app.invoke(state)
    assert out["intent"] == "pricing_intel"
    assert "BusinessPricingAgent" in [t["agent"] for t in out["agent_trace"]]
    assert out["analytics_data"] is not None
    assert "elasticity_simulation" in out["analytics_data"]

def test_business_sentiment_agent():
    state = create_initial_state("What are customer sentiment complaints regarding display?", mode="business")
    out = multi_agent_app.invoke(state)
    assert out["intent"] == "sentiment_intel"
    assert "BusinessSentimentAgent" in [t["agent"] for t in out["agent_trace"]]

def test_business_trends_agent():
    state = create_initial_state("Show monthly GMV and demand trends", mode="business")
    out = multi_agent_app.invoke(state)
    assert out["intent"] == "market_trends"
    assert "BusinessTrendsAgent" in [t["agent"] for t in out["agent_trace"]]
