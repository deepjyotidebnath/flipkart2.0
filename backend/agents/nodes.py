"""
Specialized Agent Nodes for LangGraph Orchestration:
1. RouterNode - extracts intent & entities
2. DiscoveryAgent - uses Hybrid RAG for semantic catalog discovery
3. ComparisonAgent - creates side-by-side spec & review comparison matrices
4. EvaluationAgent - scores and recommends optimal product for user constraints
5. BusinessPricingAgent - competitor gap and price elasticity analysis
6. BusinessSentimentAgent - aspect-level sentiment breakdown
7. SynthesizerNode - integrates multi-agent insights into user-friendly responses
"""

import re
import json
from typing import Dict, Any, List
from backend.agents.state import AgentState
from backend.engine.rag import rag_engine
from backend.engine.analytics import analytics_engine

def router_node(state: AgentState) -> Dict[str, Any]:
    """
    Analyzes user query and mode to determine intent and routing.
    """
    query = state.get("user_query", "").strip()
    q_lower = query.lower()
    mode = state.get("mode", "shopping")

    entities = {
        "budget": None,
        "brands": [],
        "category": None,
        "product_names": []
    }

    # Extract price constraints: "under 30000", "below 50,000", "budget 80k", "< 25000"
    price_match = re.search(r'(?:under|below|less than|within|budget of|max|budget)\s*(?:₹|rs\.?|inr)?\s*([0-9]+(?:,[0-9]+)*(?:\s*k)?)', q_lower)
    if price_match:
        val_str = price_match.group(1).replace(",", "").strip()
        if val_str.endswith("k"):
            budget_val = float(val_str[:-1]) * 1000
        else:
            budget_val = float(val_str)
        entities["budget"] = budget_val

    # Detect known brands
    known_brands = ["apple", "samsung", "oneplus", "realme", "motorola", "poco", "asus", "dell", "lenovo", "hp", "sony", "boat", "noise", "lg", "xiaomi", "puma", "nike", "levi's", "dyson", "philips"]
    for b in known_brands:
        if b in q_lower:
            entities["brands"].append(b.title())

    # Detect category
    if any(k in q_lower for k in ["phone", "mobile", "smartphone", "5g", "android", "iphone"]):
        entities["category"] = "Mobiles"
    elif any(k in q_lower for k in ["laptop", "macbook", "notebook", "gaming pc", "ultrabook"]):
        entities["category"] = "Laptops"
    elif any(k in q_lower for k in ["headphone", "earphone", "earbuds", "speaker", "soundbar", "audio", "tws"]):
        entities["category"] = "Audio"
    elif any(k in q_lower for k in ["watch", "smartwatch", "wearable", "band"]):
        entities["category"] = "Wearables"
    elif any(k in q_lower for k in ["tv", "television", "ac", "refrigerator", "fridge", "washing machine", "microwave", "air fryer"]):
        entities["category"] = "Appliances"
    elif any(k in q_lower for k in ["shoes", "sneakers", "jeans", "shirt", "jacket", "fashion"]):
        entities["category"] = "Fashion"

    # Intent classification
    if mode == "business":
        if any(k in q_lower for k in ["price", "pricing", "competitor", "elasticity", "margin", "discount", "amazon", "croma"]):
            intent = "pricing_intel"
        elif any(k in q_lower for k in ["review", "sentiment", "aspect", "complaint", "feedback", "rating", "battery life"]):
            intent = "sentiment_intel"
        elif any(k in q_lower for k in ["trend", "gmv", "demand", "stock", "inventory", "sales", "velocity"]):
            intent = "market_trends"
        else:
            intent = "pricing_intel"
    else:
        # Shopping mode
        # Match evaluation phrases first so words like "worth" or "for" aren't confused
        if any(k in q_lower for k in ["is it good", "worth buying", "worth it", "review", "should i buy", "battery life of", "rating of", "evaluate"]):
            intent = "evaluate"
        elif any(k in q_lower for k in ["compare", " vs ", "versus", "difference between"]):
            intent = "compare"
        else:
            intent = "discovery"

    trace_entry = {
        "agent": "RouterAgent",
        "action": f"Classified intent as '{intent}' in '{mode}' mode.",
        "details": {
            "intent": intent,
            "detected_entities": entities
        }
    }

    return {
        "intent": intent,
        "entities": entities,
        "agent_trace": [trace_entry]
    }


def discovery_agent(state: AgentState) -> Dict[str, Any]:
    """
    Discovers top product candidates using Hybrid RAG.
    """
    query = state.get("user_query", "")
    entities = state.get("entities", {})
    budget = entities.get("budget")
    category = entities.get("category")
    brand = entities.get("brands")[0] if entities.get("brands") else None

    # Retrieve products via hybrid RAG
    results = rag_engine.search(
        query=query,
        category=category,
        max_price=budget,
        brand=brand,
        top_k=4
    )

    # Fallback to broader search if constrained search returned nothing
    if not results:
        results = rag_engine.search(query=query, top_k=4)

    trace_entry = {
        "agent": "DiscoveryAgent",
        "action": f"Retrieved {len(results)} relevant products using Hybrid RAG (TF-IDF + BM25).",
        "details": {
            "top_matches": [r.get("title") for r in results]
        }
    }

    return {
        "retrieved_products": results,
        "recommended_products": results,
        "agent_trace": [trace_entry]
    }


def comparison_agent(state: AgentState) -> Dict[str, Any]:
    """
    Performs side-by-side feature comparison between products referenced in query or retrieved.
    """
    query = state.get("user_query", "")
    q_lower = query.lower()

    # Split on "vs" or "compare"
    items = []
    if "vs" in q_lower:
        parts = q_lower.split("vs")
        for p in parts[:2]:
            clean = p.replace("compare", "").strip()
            hits = rag_engine.search(clean, top_k=1)
            if hits:
                items.append(hits[0])
    else:
        items = rag_engine.search(query, top_k=2)

    if len(items) < 2:
        # Fallback to 2 related items
        cat = items[0]["category"] if items else None
        items = rag_engine.search(query, category=cat, top_k=2)

    comp_matrix = {}
    if len(items) >= 2:
        p1, p2 = items[0], items[1]
        all_spec_keys = set(p1.get("specs", {}).keys()).union(set(p2.get("specs", {}).keys()))

        matrix_rows = []
        for key in sorted(all_spec_keys):
            matrix_rows.append({
                "feature": key,
                "item1_value": p1.get("specs", {}).get(key, "N/A"),
                "item2_value": p2.get("specs", {}).get(key, "N/A")
            })

        price_diff = p1["price"] - p2["price"]
        verdict = ""
        if price_diff > 0:
            verdict = f"{p2['title']} is ₹{abs(price_diff):,.0f} more affordable, while {p1['title']} offers premium flagship hardware."
        else:
            verdict = f"{p1['title']} offers superior value at ₹{abs(price_diff):,.0f} less than {p2['title']}."

        comp_matrix = {
            "product_a": p1,
            "product_b": p2,
            "specs_matrix": matrix_rows,
            "verdict": verdict
        }

    trace_entry = {
        "agent": "ComparisonAgent",
        "action": f"Synthesized comparison matrix for {[it['title'] for it in items[:2]]}.",
        "details": {
            "compared_products": [it["title"] for it in items[:2]]
        }
    }

    return {
        "retrieved_products": items,
        "recommended_products": items,
        "comparison_data": comp_matrix,
        "agent_trace": [trace_entry]
    }


def evaluation_agent(state: AgentState) -> Dict[str, Any]:
    """
    Evaluates customer reviews, ratings, pros and cons to form an evidence-grounded recommendation.
    """
    query = state.get("user_query", "")
    products = rag_engine.search(query, top_k=1)
    target = products[0] if products else None

    eval_data = {}
    if target:
        # Retrieve review chunks specifically for this product
        reviews = target.get("reviews", [])
        pros = []
        cons = []
        for r in reviews:
            asp = r.get("aspects", {})
            for a, s in asp.items():
                if s > 0.5 and a not in pros:
                    pros.append(a)
                elif s < 0 and a not in cons:
                    cons.append(a)

        eval_data = {
            "product": target,
            "rating": target["rating"],
            "rating_count": target["rating_count"],
            "pros": pros if pros else ["Build quality", "Performance", "Value for Money"],
            "cons": cons if cons else ["High competition in category"],
            "review_count": len(reviews),
            "recommendation": "Highly Recommended" if target["rating"] >= 4.4 else "Solid Buy with Minor Caveats"
        }

    trace_entry = {
        "agent": "EvaluationAgent",
        "action": f"Evaluated customer feedback and sentiments for {target['title'] if target else 'item'}.",
        "details": eval_data
    }

    return {
        "retrieved_products": [target] if target else [],
        "recommended_products": [target] if target else [],
        "analytics_data": eval_data,
        "agent_trace": [trace_entry]
    }


def business_pricing_agent(state: AgentState) -> Dict[str, Any]:
    """
    Performs competitive price benchmarking and elasticity calculations for merchants.
    """
    query = state.get("user_query", "")
    benchmarks = analytics_engine.compute_competitor_benchmarks()

    # Check if a specific product was mentioned
    hits = rag_engine.search(query, top_k=1)
    target_pid = hits[0]["id"] if hits else "MOB-APPL-IP15"

    elasticity = analytics_engine.simulate_price_elasticity(target_pid, 0.0)

    # Relevant competitor gap
    rel_gap = next((b for b in benchmarks if b["product_id"] == target_pid), benchmarks[0] if benchmarks else None)

    pricing_payload = {
        "benchmarks_sample": benchmarks[:6],
        "target_product_gap": rel_gap,
        "elasticity_simulation": elasticity
    }

    trace_entry = {
        "agent": "BusinessPricingAgent",
        "action": f"Calculated price elasticity curve and competitor gap against Amazon & Croma.",
        "details": {
            "target_product": elasticity.get("title"),
            "elasticity": elasticity.get("elasticity_coefficient"),
            "optimal_discount": elasticity.get("optimal_recommendation", {}).get("optimal_discount_pct")
        }
    }

    return {
        "analytics_data": pricing_payload,
        "agent_trace": [trace_entry]
    }


def business_sentiment_agent(state: AgentState) -> Dict[str, Any]:
    """
    Aggregates aspect-level customer feedback to reveal satisfaction drivers and pain points.
    """
    sentiment_data = analytics_engine.compute_sentiment_breakdown()

    trace_entry = {
        "agent": "BusinessSentimentAgent",
        "action": "Extracted aspect sentiment radar (Battery, Display, Performance, Camera, Value).",
        "details": {
            "top_aspects": [a["aspect"] for a in sentiment_data.get("aspect_breakdown", [])[:5]]
        }
    }

    return {
        "analytics_data": sentiment_data,
        "agent_trace": [trace_entry]
    }


def business_trends_agent(state: AgentState) -> Dict[str, Any]:
    """
    Analyzes category velocity, GMV contribution, and inventory stock-out risks.
    """
    trends = analytics_engine.compute_market_trends()

    trace_entry = {
        "agent": "BusinessTrendsAgent",
        "action": "Computed category demand velocity and identified critical inventory stock-out risks.",
        "details": {
            "critical_stock_alerts_count": len([x for x in trends.get("inventory_risk_alerts", []) if x["risk_level"] == "CRITICAL"])
        }
    }

    return {
        "analytics_data": trends,
        "agent_trace": [trace_entry]
    }


def synthesizer_node(state: AgentState) -> Dict[str, Any]:
    """
    Combines agent findings into a crisp, authoritative response with suggested follow-up actions.
    """
    intent = state.get("intent", "discovery")
    mode = state.get("mode", "shopping")
    products = state.get("recommended_products", [])
    comp = state.get("comparison_data")
    analytics = state.get("analytics_data")
    query = state.get("user_query", "")

    suggestions = []

    if mode == "business":
        if intent == "pricing_intel":
            sim = analytics.get("elasticity_simulation", {})
            gap = analytics.get("target_product_gap", {})
            opt = sim.get("optimal_recommendation", {})

            response = (
                f"### 📊 Competitive Pricing & Margin Intelligence\n\n"
                f"**Product:** {sim.get('title', 'Target Product')}\n"
                f"- **Current Flipkart Price:** ₹{sim.get('current_price', 0):,.0f} ({sim.get('current_discount_pct', 0)}% off)\n"
                f"- **Competitor Price Benchmark:** ₹{gap.get('lowest_competitor_price', 0):,.0f} (Status: {gap.get('status', 'Parity')})\n"
                f"- **Price Elasticity (PED):** {sim.get('elasticity_coefficient', 1.5):.2f} (Elastic Demand)\n\n"
                f"**🎯 AI Pricing Recommendation:**\n"
                f"Setting discount to **{opt.get('optimal_discount_pct', 0)}%** (Price: ₹{opt.get('optimal_price', 0):,.0f}) is projected to maximize monthly gross profit to **₹{opt.get('projected_profit', 0):,.0f}** across {opt.get('projected_units', 0):,} units.\n"
            )
            suggestions = [
                "Run discount simulation at +5%",
                "Show aspect sentiment complaints",
                "View inventory stock-out risks"
            ]

        elif intent == "sentiment_intel":
            aspects = analytics.get("aspect_breakdown", [])
            top_aspects_txt = "\n".join([f"- **{a['aspect']}**: {a['positive_pct']}% Positive sentiment ({a['mention_count']} mentions)" for a in aspects[:4]])
            response = (
                f"### 💬 Customer Review & Aspect Sentiment Analysis\n\n"
                f"Aggregated customer satisfaction across verified Flipkart buyer reviews:\n\n"
                f"{top_aspects_txt}\n\n"
                f"**💡 Key Insight:** Build Quality and Value for Money are primary delight drivers, while Battery Performance receives mixed feedback in high-performance items."
            )
            suggestions = [
                "Which smartphones have the best battery reviews?",
                "Analyze competitor price gaps",
                "Show category GMV breakdown"
            ]

        else: # market_trends
            cat_trends = analytics.get("category_trends", [])
            alerts = analytics.get("inventory_risk_alerts", [])
            top_cat = cat_trends[0] if cat_trends else {}
            crit_alerts = [a for a in alerts if a["risk_level"] == "CRITICAL"]

            response = (
                f"### 📈 Market Trends & Demand Velocity\n\n"
                f"- **Leading Category:** {top_cat.get('category', 'Electronics')} with **₹{top_cat.get('total_gmv', 0):,.0f}** monthly GMV and {top_cat.get('units_sold', 0):,} units.\n"
                f"- **Inventory Risk Warning:** **{len(crit_alerts)} items** have under 3 days of remaining stock based on daily burn rate.\n"
            )
            suggestions = [
                "Show critical stock reorder list",
                "Compare Flipkart prices vs Amazon",
                "Simulate discount on high-stock items"
            ]

    else:
        # Shopping Assistant Mode
        if intent == "compare" and comp:
            p1 = comp.get("product_a", {})
            p2 = comp.get("product_b", {})
            response = (
                f"### ⚖️ Side-by-Side Product Comparison\n\n"
                f"Comparing **{p1.get('title')}** vs **{p2.get('title')}**:\n\n"
                f"- **{p1.get('title')}**: ₹{p1.get('price', 0):,.0f} ({p1.get('rating', 0)}★)\n"
                f"- **{p2.get('title')}**: ₹{p2.get('price', 0):,.0f} ({p2.get('rating', 0)}★)\n\n"
                f"**💡 Verdict:** {comp.get('verdict')}\n"
            )
            suggestions = [
                f"Show user reviews for {p1.get('title', '').split()[0]}",
                f"Show user reviews for {p2.get('title', '').split()[0]}",
                "Show other options in this price range"
            ]

        elif intent == "evaluate" and analytics:
            prod = analytics.get("product", {})
            pros = ", ".join(analytics.get("pros", []))
            cons = ", ".join(analytics.get("cons", []))
            response = (
                f"### 🔍 Product Evaluation: {prod.get('title')}\n\n"
                f"- **Current Flipkart Price:** ₹{prod.get('price', 0):,.0f} ({prod.get('discount_pct', 0)}% off MRP ₹{prod.get('original_price', 0):,.0f})\n"
                f"- **Customer Rating:** {prod.get('rating', 0)}★ ({prod.get('rating_count', 0):,} verified reviews)\n\n"
                f"**👍 Key Strengths:** {pros}\n"
                f"**⚠️ Consideration:** {cons}\n\n"
                f"**Flipkart Intelligence Verdict:** **{analytics.get('recommendation')}**."
            )
            suggestions = [
                f"Compare {prod.get('title', '').split()[0]} with competitors",
                f"What are the best alternatives under ₹{prod.get('price', 0):,.0f}?",
                "Check delivery timeline and offers"
            ]

        else: # discovery
            if products:
                top_item = products[0]
                items_summary = "\n".join([
                    f"- **{p['title']}** — ₹{p['price']:,.0f} (⭐ {p['rating']} | {p['discount_pct']}% OFF)"
                    for p in products[:3]
                ])
                response = (
                    f"Here are top-rated recommendations tailored to your query:\n\n"
                    f"{items_summary}\n\n"
                    f"Our top pick is **{top_item['title']}** featuring {', '.join(top_item.get('features', [])[:2])}."
                )
            else:
                response = "I searched the Flipkart catalog but could not find exact matches for your query. Try searching by brand, budget, or specifications."

            suggestions = [
                "Show best camera phone under ₹30,000",
                "Compare MacBook Air M2 vs Dell XPS 13",
                "Top rated noise cancelling headphones"
            ]

    trace_entry = {
        "agent": "SynthesizerNode",
        "action": "Generated structured markdown synthesis with recommended cards and quick prompts.",
        "details": {"product_count": len(products)}
    }

    return {
        "final_response": response,
        "recommended_products": products,
        "quick_suggestions": suggestions,
        "agent_trace": [trace_entry]
    }
