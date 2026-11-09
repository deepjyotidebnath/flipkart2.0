"""
ML Analytics Suite for E-commerce Business Intelligence:
1. Aspect & Polarity Sentiment Mining
2. Price Elasticity & Revenue/Margin Simulation
3. Competitor Price Gap & Benchmark Analysis
4. Market Demand, Sales Velocity, & Stock Out Risk Forecasting
"""

import json
import math
from typing import List, Dict, Any, Optional
import numpy as np
from backend.data.db import get_connection

class AnalyticsEngine:
    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path

    def get_all_products(self) -> List[Dict[str, Any]]:
        conn = get_connection(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM products")
        products = [dict(row) for row in cur.fetchall()]
        conn.close()
        for p in products:
            p["specs"] = json.loads(p.get("specs_json", "{}"))
            p["features"] = json.loads(p.get("features_json", "[]"))
        return products

    def get_all_competitor_prices(self) -> List[Dict[str, Any]]:
        conn = get_connection(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM competitor_prices")
        comps = [dict(row) for row in cur.fetchall()]
        conn.close()
        return comps

    def get_all_reviews(self) -> List[Dict[str, Any]]:
        conn = get_connection(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM reviews")
        reviews = [dict(row) for row in cur.fetchall()]
        conn.close()
        for r in reviews:
            r["aspects"] = json.loads(r.get("aspects_json", "{}"))
        return reviews

    def compute_executive_overview(self) -> Dict[str, Any]:
        """
        Calculates high-level executive KPIs across the entire Flipkart catalog.
        """
        products = self.get_all_products()
        comps = self.get_all_competitor_prices()
        reviews = self.get_all_reviews()

        total_products = len(products)
        total_monthly_gmv = sum(p["price"] * p["monthly_sales_units"] for p in products)
        total_monthly_profit = sum((p["price"] - p["cost_price"]) * p["monthly_sales_units"] for p in products)
        avg_margin_pct = (total_monthly_profit / total_monthly_gmv * 100) if total_monthly_gmv > 0 else 0.0

        avg_discount_pct = np.mean([p["discount_pct"] for p in products]) if products else 0.0
        avg_rating = np.mean([p["rating"] for p in products]) if products else 0.0

        # Competitor Price Advantage
        # Compare Flipkart price vs lowest competitor price for shared items
        comp_map = {}
        for c in comps:
            pid = c["product_id"]
            if pid not in comp_map:
                comp_map[pid] = []
            comp_map[pid].append(c["price"])

        advantage_wins = 0
        total_comparable = 0
        for p in products:
            pid = p["id"]
            if pid in comp_map and comp_map[pid]:
                lowest_comp = min(comp_map[pid])
                total_comparable += 1
                if p["price"] <= lowest_comp:
                    advantage_wins += 1

        price_competitiveness_index = (advantage_wins / total_comparable * 100) if total_comparable > 0 else 85.0

        # Overall sentiment score from reviews
        sentiments = []
        for r in reviews:
            asp = r["aspects"]
            if asp:
                sentiments.extend(asp.values())
            else:
                sentiments.append((r["rating"] - 3.0) / 2.0)
        overall_sentiment_score = float(np.mean(sentiments)) if sentiments else 0.75

        return {
            "total_products": total_products,
            "monthly_gmv_inr": round(total_monthly_gmv, 2),
            "monthly_profit_inr": round(total_monthly_profit, 2),
            "avg_margin_pct": round(avg_margin_pct, 1),
            "avg_discount_pct": round(avg_discount_pct, 1),
            "avg_rating": round(avg_rating, 2),
            "price_competitiveness_index": round(price_competitiveness_index, 1),
            "overall_sentiment_score": round(overall_sentiment_score, 2),
            "total_reviews": len(reviews)
        }

    def compute_competitor_benchmarks(self) -> List[Dict[str, Any]]:
        """
        Analyzes competitor pricing gaps across Amazon, Croma, Reliance Digital.
        """
        products = self.get_all_products()
        comps = self.get_all_competitor_prices()

        comps_by_pid = {}
        for c in comps:
            pid = c["product_id"]
            if pid not in comps_by_pid:
                comps_by_pid[pid] = []
            comps_by_pid[pid].append(c)

        benchmarks = []
        for p in products:
            pid = p["id"]
            p_comps = comps_by_pid.get(pid, [])
            if not p_comps:
                continue

            comp_prices = [c["price"] for c in p_comps]
            min_comp = min(comp_prices)
            avg_comp = float(np.mean(comp_prices))
            price_gap_pct = ((p["price"] - min_comp) / min_comp) * 100

            status = "Best Price" if p["price"] < min_comp else ("Parity" if p["price"] == min_comp else "Overpriced")

            benchmarks.append({
                "product_id": pid,
                "title": p["title"],
                "category": p["category"],
                "flipkart_price": p["price"],
                "lowest_competitor_price": min_comp,
                "avg_competitor_price": round(avg_comp, 2),
                "price_gap_pct": round(price_gap_pct, 2),
                "status": status,
                "competitors": p_comps
            })

        benchmarks.sort(key=lambda x: x["price_gap_pct"])
        return benchmarks

    def compute_sentiment_breakdown(self) -> Dict[str, Any]:
        """
        Extracts aspect-level sentiment metrics across categories and product lines.
        """
        reviews = self.get_all_reviews()
        products = self.get_all_products()
        prod_map = {p["id"]: p for p in products}

        aspect_aggregates: Dict[str, List[float]] = {}
        category_sentiment: Dict[str, List[float]] = {}
        product_sentiment: Dict[str, Dict[str, Any]] = {}

        for r in reviews:
            pid = r["product_id"]
            p_info = prod_map.get(pid, {})
            cat = p_info.get("category", "General")

            asp = r.get("aspects", {})
            for aspect_name, score in asp.items():
                if aspect_name not in aspect_aggregates:
                    aspect_aggregates[aspect_name] = []
                aspect_aggregates[aspect_name].append(score)

            # Record category sentiment
            avg_rev_score = float(np.mean(list(asp.values()))) if asp else (r["rating"] - 3.0) / 2.0
            if cat not in category_sentiment:
                category_sentiment[cat] = []
            category_sentiment[cat].append(avg_rev_score)

            if pid not in product_sentiment:
                product_sentiment[pid] = {
                    "product_id": pid,
                    "title": p_info.get("title", pid),
                    "category": cat,
                    "scores": [],
                    "positive_count": 0,
                    "negative_count": 0,
                    "total_count": 0
                }
            product_sentiment[pid]["scores"].append(avg_rev_score)
            product_sentiment[pid]["total_count"] += 1
            if avg_rev_score >= 0.2:
                product_sentiment[pid]["positive_count"] += 1
            elif avg_rev_score <= -0.2:
                product_sentiment[pid]["negative_count"] += 1

        # Format Aspect Radar / Bar metrics
        aspect_summary = []
        for aspect, scores in aspect_aggregates.items():
            pos = sum(1 for s in scores if s > 0.2)
            neg = sum(1 for s in scores if s < -0.2)
            neu = len(scores) - pos - neg
            aspect_summary.append({
                "aspect": aspect,
                "avg_score": round(float(np.mean(scores)), 2),
                "positive_pct": round((pos / len(scores)) * 100, 1),
                "negative_pct": round((neg / len(scores)) * 100, 1),
                "neutral_pct": round((neu / len(scores)) * 100, 1),
                "mention_count": len(scores)
            })
        aspect_summary.sort(key=lambda x: x["mention_count"], reverse=True)

        cat_summary = []
        for cat, scores in category_sentiment.items():
            cat_summary.append({
                "category": cat,
                "avg_score": round(float(np.mean(scores)), 2),
                "review_count": len(scores)
            })

        prod_list = []
        for pid, data in product_sentiment.items():
            avg_s = float(np.mean(data["scores"])) if data["scores"] else 0.0
            prod_list.append({
                "product_id": pid,
                "title": data["title"],
                "category": data["category"],
                "avg_sentiment": round(avg_s, 2),
                "positive_pct": round((data["positive_count"] / max(data["total_count"], 1)) * 100, 1),
                "total_reviews": data["total_count"]
            })
        prod_list.sort(key=lambda x: x["avg_sentiment"], reverse=True)

        return {
            "aspect_breakdown": aspect_summary,
            "category_sentiment": cat_summary,
            "product_sentiment": prod_list[:10]
        }

    def simulate_price_elasticity(
        self,
        product_id: str,
        discount_pct_delta: float
    ) -> Dict[str, Any]:
        """
        Simulates how changing discount / price affects sales volume, revenue, and gross profit.
        Uses standard Constant Elasticity of Demand (PED) model:
        % ΔQ = - Elasticity * % ΔP
        """
        conn = get_connection(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cur.fetchone()
        conn.close()

        if not row:
            return {"error": "Product not found"}

        p = dict(row)
        orig_price = p["original_price"]
        current_price = p["price"]
        cost_price = p["cost_price"]
        current_units = p["monthly_sales_units"]

        # Category elasticity coefficient
        cat = p["category"].lower()
        if "mobile" in cat or "smartphone" in cat:
            ped = 1.6  # High elasticity
        elif "laptop" in cat:
            ped = 1.4
        elif "audio" in cat or "wearable" in cat:
            ped = 2.1  # Very high elasticity in lifestyle accessories
        elif "fashion" in cat:
            ped = 2.4
        else:
            ped = 1.3

        current_discount_pct = p["discount_pct"]
        new_discount_pct = max(0.0, min(85.0, current_discount_pct + discount_pct_delta))
        new_price = round(orig_price * (1.0 - (new_discount_pct / 100.0)), 2)

        # % change in price
        price_change_pct = ((new_price - current_price) / current_price)
        # Expected % change in quantity demanded
        demand_change_pct = -ped * price_change_pct
        new_units = max(10, int(round(current_units * (1.0 + demand_change_pct))))

        current_revenue = current_price * current_units
        current_profit = (current_price - cost_price) * current_units

        new_revenue = new_price * new_units
        new_profit = (new_price - cost_price) * new_units

        revenue_delta_pct = ((new_revenue - current_revenue) / current_revenue) * 100
        profit_delta_pct = ((new_profit - current_profit) / (current_profit + 1e-5)) * 100

        # Generate price vs profit curve across a range of discounts [0% to 50%]
        curve = []
        for disc in range(0, 55, 5):
            sim_p = orig_price * (1.0 - (disc / 100.0))
            sim_pchg = (sim_p - current_price) / current_price
            sim_q = max(5, int(round(current_units * (1.0 - ped * sim_pchg))))
            sim_rev = sim_p * sim_q
            sim_prof = (sim_p - cost_price) * sim_q
            curve.append({
                "discount_pct": disc,
                "price": round(sim_p, 2),
                "units": sim_q,
                "revenue": round(sim_rev, 2),
                "profit": round(sim_prof, 2)
            })

        # Find optimal discount maximizing profit
        optimal_point = max(curve, key=lambda x: x["profit"])

        return {
            "product_id": product_id,
            "title": p["title"],
            "elasticity_coefficient": ped,
            "current_price": current_price,
            "cost_price": cost_price,
            "current_discount_pct": current_discount_pct,
            "current_units": current_units,
            "current_revenue": round(current_revenue, 2),
            "current_profit": round(current_profit, 2),
            "simulated_discount_pct": round(new_discount_pct, 1),
            "simulated_price": new_price,
            "simulated_units": new_units,
            "simulated_revenue": round(new_revenue, 2),
            "simulated_profit": round(new_profit, 2),
            "revenue_delta_pct": round(revenue_delta_pct, 2),
            "profit_delta_pct": round(profit_delta_pct, 2),
            "optimal_recommendation": {
                "optimal_discount_pct": optimal_point["discount_pct"],
                "optimal_price": optimal_point["price"],
                "projected_profit": optimal_point["profit"],
                "projected_revenue": optimal_point["revenue"],
                "projected_units": optimal_point["units"]
            },
            "elasticity_curve": curve
        }

    def compute_market_trends(self) -> Dict[str, Any]:
        """
        Computes category demand trends, stock burn rates, and inventory risk alerts.
        """
        products = self.get_all_products()
        categories: Dict[str, Dict[str, Any]] = {}

        inventory_alerts = []

        for p in products:
            cat = p["category"]
            if cat not in categories:
                categories[cat] = {
                    "category": cat,
                    "total_gmv": 0.0,
                    "units_sold": 0,
                    "avg_rating": [],
                    "product_count": 0
                }
            units = p["monthly_sales_units"]
            categories[cat]["total_gmv"] += (p["price"] * units)
            categories[cat]["units_sold"] += units
            categories[cat]["avg_rating"].append(p["rating"])
            categories[cat]["product_count"] += 1

            # Inventory risk analysis: stock / (units / 30) = days of cover
            daily_burn = max(1.0, units / 30.0)
            days_of_stock = p["stock"] / daily_burn
            if days_of_stock < 7:
                inventory_alerts.append({
                    "product_id": p["id"],
                    "title": p["title"],
                    "category": p["category"],
                    "stock": p["stock"],
                    "daily_burn": round(daily_burn, 1),
                    "days_of_stock": round(days_of_stock, 1),
                    "risk_level": "CRITICAL" if days_of_stock < 3 else "WARNING",
                    "action": "Immediate Reorder Required" if days_of_stock < 3 else "Review Restock Schedule"
                })

        category_trends = []
        for cat, data in categories.items():
            category_trends.append({
                "category": cat,
                "total_gmv": round(data["total_gmv"], 2),
                "units_sold": data["units_sold"],
                "avg_rating": round(float(np.mean(data["avg_rating"])), 2),
                "product_count": data["product_count"],
                "growth_velocity_index": round(100.0 * (data["total_gmv"] / 10000000.0), 1)
            })
        category_trends.sort(key=lambda x: x["total_gmv"], reverse=True)
        inventory_alerts.sort(key=lambda x: x["days_of_stock"])

        return {
            "category_trends": category_trends,
            "inventory_risk_alerts": inventory_alerts
        }

# Global singleton instance
analytics_engine = AnalyticsEngine()
