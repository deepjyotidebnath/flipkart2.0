"""
Adds additional diverse products to reach 50+ items and expands reviews dataset.
"""
from backend.data.db import get_connection
import json
import random

MORE_ITEMS = [
    {
        "id": "AUD-MARS-EMBER",
        "title": "Marshall Emberton II Portable Bluetooth Speaker (Black and Brass)",
        "brand": "Marshall",
        "category": "Audio",
        "sub_category": "Bluetooth Speakers",
        "price": 14999.0,
        "original_price": 19999.0,
        "discount_pct": 25.0,
        "rating": 4.7,
        "rating_count": 8900,
        "stock": 30,
        "cost_price": 11500.0,
        "monthly_sales_units": 620,
        "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=600&auto=format&fit=crop&q=80",
        "description": "Iconic vintage rock-and-roll Marshall styling, 30+ hours of portable playtime, IP67 dust and water resistance, True Stereophonic 360 sound.",
        "specs": {"Playtime": "30+ Hours", "Water Resistance": "IP67", "Weight": "0.7 kg", "Sound": "True Stereophonic multi-directional sound"},
        "features": ["30+ Hours of Portable Playtime", "Stack Mode Linking", "Iconic Marshall Script & Brass Controls", "IP67 Waterproof"]
    },
    {
        "id": "LAP-DELL-INSP54",
        "title": "DELL Inspiron 14 Intel Core i5 13th Gen (16 GB RAM, 512 GB SSD, Thin & Light)",
        "brand": "DELL",
        "category": "Laptops",
        "sub_category": "Everyday / Student",
        "price": 57990.0,
        "original_price": 72990.0,
        "discount_pct": 20.6,
        "rating": 4.3,
        "rating_count": 15400,
        "stock": 50,
        "cost_price": 48000.0,
        "monthly_sales_units": 1250,
        "image_url": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop&q=80",
        "description": "Crisp 14-inch 16:10 FHD+ anti-glare display, Intel 13th Gen Core i5-1335U, fingerprint reader, backlit keyboard, and ExpressCharge.",
        "specs": {"Processor": "Intel Core i5-1335U", "RAM": "16 GB DDR5", "Storage": "512 GB M.2 NVMe SSD", "Display": "14.0 inch 16:10 FHD+ (1920 x 1200)", "Weight": "1.54 kg"},
        "features": ["16:10 Aspect Ratio Display", "ExpressCharge 80% in 60 mins", "Fingerprint Reader", "Waves MaxxAudio Pro"]
    },
    {
        "id": "HOME-PHIL-AIR",
        "title": "Philips Digital Air Fryer HD9252/90 (4.1 L, Rapid Air Technology, Touchscreen)",
        "brand": "Philips",
        "category": "Appliances",
        "sub_category": "Kitchen Appliances",
        "price": 6999.0,
        "original_price": 11995.0,
        "discount_pct": 41.6,
        "rating": 4.5,
        "rating_count": 54200,
        "stock": 75,
        "cost_price": 5100.0,
        "monthly_sales_units": 3100,
        "image_url": "https://images.unsplash.com/photo-1584992236310-6edddc08acff?w=600&auto=format&fit=crop&q=80",
        "description": "Fry with up to 90% less fat. Patented Rapid Air starfish design circulates hot air for crispy outside and tender inside. 7 preset touchscreen menus.",
        "specs": {"Capacity": "4.1 Litres (0.8 kg fries)", "Power": "1400W", "Presets": "7 Touchscreen presets", "Dishwasher Safe": "Yes, removable parts"},
        "features": ["Patented Rapid Air Starfish Technology", "7 Preset Menus with Keep Warm", "Up to 90% Less Fat", "NutriU App Recipe Integration"]
    },
    {
        "id": "HOME-AQUA-RO",
        "title": "Aquaguard Sure Delight NXT RO+UV Water Purifier (6L Stainless Steel / Food Grade)",
        "brand": "Eureka Forbes",
        "category": "Appliances",
        "sub_category": "Water Purifiers",
        "price": 8999.0,
        "original_price": 14000.0,
        "discount_pct": 35.7,
        "rating": 4.3,
        "rating_count": 38100,
        "stock": 90,
        "cost_price": 6800.0,
        "monthly_sales_units": 2400,
        "image_url": "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=600&auto=format&fit=crop&q=80",
        "description": "Best-in-class multi-stage RO+UV purification with Taste Adjuster (MTDS) providing sweet-tasting water from municipal, tanker, and borewell water.",
        "specs": {"Purification": "RO + UV + MTDS (Taste Adjuster)", "Capacity": "6 Litres storage", "Stages": "6 Stage purification", "Suitable for": "TDS up to 2000 mg/L"},
        "features": ["Taste Adjuster for All Water Sources", "UV e-boiling Equivalent to 20 mins boiled water", "Energy Saving Smart Shut-off"]
    },
    {
        "id": "FASH-WROGN-SHIRT",
        "title": "WROGN Men Slim Fit Checked Casual Cotton Shirt (Navy & White)",
        "brand": "WROGN",
        "category": "Fashion",
        "sub_category": "Men's Clothing",
        "price": 1199.0,
        "original_price": 2799.0,
        "discount_pct": 57.2,
        "rating": 4.2,
        "rating_count": 27400,
        "stock": 160,
        "cost_price": 650.0,
        "monthly_sales_units": 3900,
        "image_url": "https://images.unsplash.com/photo-1598033129183-c4f50c736f10?w=600&auto=format&fit=crop&q=80",
        "description": "100% pure combed cotton slim fit casual shirt with signature curved hem, spread collar, and contrast button stitching.",
        "specs": {"Fabric": "100% Breathable Cotton", "Fit": "Slim Fit", "Pattern": "Grid Checkered", "Collar": "Spread Collar"},
        "features": ["100% Combed Cotton Soft Touch", "Curved Hemline for untucked styling", "Reinforced Stitching"]
    },
    {
        "id": "FASH-FAST-WATCH",
        "title": "Fastrack Limitless FS1 Pro Smartwatch (1.96-inch AMOLED Display, Arched Design)",
        "brand": "Fastrack",
        "category": "Wearables",
        "sub_category": "Smartwatch",
        "price": 1999.0,
        "original_price": 7995.0,
        "discount_pct": 75.0,
        "rating": 4.2,
        "rating_count": 91200,
        "stock": 220,
        "cost_price": 1200.0,
        "monthly_sales_units": 7800,
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80",
        "description": "India's largest 1.96-inch Super AMOLED Arched display with NitroFast charging, SingleSync BT calling, and 110+ sports modes.",
        "specs": {"Display": "1.96 inch Super AMOLED 410x502 (60Hz)", "Calling": "SingleSync Bluetooth Calling", "Battery": "Up to 7 days battery (Fast Charge in 30m)", "Water Resistance": "IP68"},
        "features": ["Arched Curved Super AMOLED Screen", "NitroFast Fast Charging", "AI Voice Assistant integration", "110+ Sports Modes"]
    },
    {
        "id": "MOB-REAL-NARZO60",
        "title": "realme Narzo 60x 5G (Stellar Green, 128 GB, 6 GB RAM)",
        "brand": "realme",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 12499.0,
        "original_price": 15999.0,
        "discount_pct": 21.9,
        "rating": 4.3,
        "rating_count": 68400,
        "stock": 130,
        "cost_price": 10200.0,
        "monthly_sales_units": 4100,
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600&auto=format&fit=crop&q=80",
        "description": "Ultra-slim 7.89mm design with InterstellarX pattern. 50MP AI primary camera, 33W SUPERVOOC charge, and 120Hz dynamic display.",
        "specs": {"RAM": "6 GB (up to 12 GB Dynamic)", "Storage": "128 GB", "Processor": "Dimensity 6100+ 5G", "Display": "6.72 inch 120Hz FHD+ Dynamic Display", "Battery": "5000 mAh (33W Flash)"},
        "features": ["7.89mm Ultra Slim Body", "33W Fast SUPERVOOC Charge", "50MP AI Camera", "Dual 5G Standby"]
    },
    {
        "id": "HOME-PREST-COOK",
        "title": "Prestige Deluxe Alpha Svachh 3 L Outer Lid Induction Base Pressure Cooker",
        "brand": "Prestige",
        "category": "Appliances",
        "sub_category": "Cookware",
        "price": 1899.0,
        "original_price": 2750.0,
        "discount_pct": 30.9,
        "rating": 4.4,
        "rating_count": 82000,
        "stock": 250,
        "cost_price": 1250.0,
        "monthly_sales_units": 5800,
        "image_url": "https://images.unsplash.com/photo-1584992236310-6edddc08acff?w=600&auto=format&fit=crop&q=80",
        "description": "Svachh deep lid controls froth spillage onto stove. Durable stainless steel Alpha base suitable for gas and induction cooking with 5-year warranty.",
        "specs": {"Capacity": "3 Litres", "Material": "Stainless Steel 304 Food Grade", "Base": "Alpha Induction Compatible Base", "Warranty": "5 Years"},
        "features": ["Spillage Control Svachh Deep Lid", "Controlled Gasket Release System", "Induction and Gas Compatible", "Cool Touch Durable Handles"]
    }
]

def add_more():
    conn = get_connection()
    cur = conn.cursor()
    for p in MORE_ITEMS:
        cur.execute("""
            INSERT OR REPLACE INTO products (
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
        cur.execute("""
            INSERT INTO competitor_prices (product_id, competitor_name, price, in_stock, delivery_days, url)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (p["id"], "Amazon", round(p["price"] * 1.02, -1), 1, 2, "https://amazon.in"))

        cur.execute("""
            INSERT INTO reviews (product_id, author, rating, title, review_text, aspects_json, verified_purchase, helpful_count, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["id"], "Verified Buyer", 4.5, "Top notch quality and performance",
            f"Superb build quality and value. Flipkart prompt delivery made this {p['title']} purchase worthwhile.",
            json.dumps({"Build": 0.9, "Value for Money": 0.9, "Delivery": 1.0}), 1, 45, "2025-01-22"
        ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_more()
    print("Added more products successfully.")
