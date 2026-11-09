"""
Flipkart Intelligence Agent - Database Layer and Seed Data Generator
Initializes SQLite database with products, competitor listings, and detailed customer reviews.
"""

import sqlite3
import json
import os
from typing import List, Dict, Any, Optional

DB_PATH = os.path.join(os.path.dirname(__file__), "flipkart.db")

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS products (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    brand TEXT NOT NULL,
    category TEXT NOT NULL,
    sub_category TEXT,
    price REAL NOT NULL,
    original_price REAL NOT NULL,
    discount_pct REAL NOT NULL,
    rating REAL NOT NULL,
    rating_count INTEGER NOT NULL,
    stock INTEGER NOT NULL,
    specs_json TEXT NOT NULL,
    description TEXT NOT NULL,
    features_json TEXT NOT NULL,
    image_url TEXT NOT NULL,
    cost_price REAL NOT NULL,
    monthly_sales_units INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS competitor_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT NOT NULL,
    competitor_name TEXT NOT NULL,
    price REAL NOT NULL,
    in_stock INTEGER NOT NULL,
    delivery_days INTEGER NOT NULL,
    url TEXT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT NOT NULL,
    author TEXT NOT NULL,
    rating REAL NOT NULL,
    title TEXT,
    review_text TEXT NOT NULL,
    aspects_json TEXT NOT NULL,
    verified_purchase INTEGER NOT NULL,
    helpful_count INTEGER DEFAULT 0,
    created_at TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE INDEX IF NOT EXISTS idx_products_cat ON products(category);
CREATE INDEX IF NOT EXISTS idx_products_brand ON products(brand);
CREATE INDEX IF NOT EXISTS idx_products_price ON products(price);
CREATE INDEX IF NOT EXISTS idx_reviews_pid ON reviews(product_id);
CREATE INDEX IF NOT EXISTS idx_comp_pid ON competitor_prices(product_id);
"""

def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    path = db_path if db_path is not None else DB_PATH
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: str = DB_PATH):
    conn = get_connection(db_path)
    with conn:
        conn.executescript(SCHEMA_SQL)
    conn.close()

def seed_db(db_path: str = DB_PATH):
    from backend.data.seed_catalog import SAMPLE_PRODUCTS, SAMPLE_REVIEWS, SAMPLE_COMPETITORS
    init_db(db_path)
    conn = get_connection(db_path)
    cursor = conn.cursor()

    # Clear existing data for clean seed
    cursor.execute("DELETE FROM competitor_prices")
    cursor.execute("DELETE FROM reviews")
    cursor.execute("DELETE FROM products")

    # Insert products
    for p in SAMPLE_PRODUCTS:
        cursor.execute("""
            INSERT INTO products (
                id, title, brand, category, sub_category, price, original_price,
                discount_pct, rating, rating_count, stock, specs_json, description,
                features_json, image_url, cost_price, monthly_sales_units
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["id"], p["title"], p["brand"], p["category"], p.get("sub_category", ""),
            p["price"], p["original_price"], p["discount_pct"], p["rating"], p["rating_count"],
            p["stock"], json.dumps(p["specs"]), p["description"], json.dumps(p["features"]),
            p["image_url"], p["cost_price"], p["monthly_sales_units"]
        ))

    # Insert competitor prices
    for c in SAMPLE_COMPETITORS:
        cursor.execute("""
            INSERT INTO competitor_prices (
                product_id, competitor_name, price, in_stock, delivery_days, url
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            c["product_id"], c["competitor_name"], c["price"],
            1 if c.get("in_stock", True) else 0,
            c.get("delivery_days", 2),
            c.get("url", "")
        ))

    # Insert reviews
    for r in SAMPLE_REVIEWS:
        cursor.execute("""
            INSERT INTO reviews (
                product_id, author, rating, title, review_text, aspects_json,
                verified_purchase, helpful_count, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            r["product_id"], r["author"], r["rating"], r["title"],
            r["review_text"], json.dumps(r.get("aspects", {})),
            1 if r.get("verified_purchase", True) else 0,
            r.get("helpful_count", 0),
            r.get("created_at", "2025-01-15")
        ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_db()
    print("Database initialized and seeded successfully.")
