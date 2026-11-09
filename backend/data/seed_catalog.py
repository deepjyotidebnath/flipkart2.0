"""
Rich, realistic product catalog, competitor benchmarks, and customer reviews dataset.
Covers 50+ diverse products across Smartphones, Laptops, Audio, Wearables, Home Appliances, and Fashion.
"""

SAMPLE_PRODUCTS = [
    # --- SMARTPHONES ---
    {
        "id": "MOB-APPL-IP15",
        "title": "Apple iPhone 15 (Blue, 128 GB)",
        "brand": "Apple",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 65999.0,
        "original_price": 79900.0,
        "discount_pct": 17.4,
        "rating": 4.6,
        "rating_count": 28410,
        "stock": 45,
        "cost_price": 56000.0,
        "monthly_sales_units": 1250,
        "image_url": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=600&auto=format&fit=crop&q=80",
        "description": "Dynamic Island bubbles up alerts and Live Activities. 48MP main camera with 2x Telephoto. Durable color-infused glass and aluminum design with USB-C connector.",
        "specs": {
            "RAM": "6 GB",
            "Storage": "128 GB",
            "Processor": "A16 Bionic chip",
            "Display": "6.1 inch Super Retina XDR OLED",
            "Rear Camera": "48MP + 12MP",
            "Front Camera": "12MP TrueDepth",
            "Battery": "3349 mAh (up to 20 hrs video)",
            "5G": "Yes",
            "OS": "iOS 17"
        },
        "features": ["Dynamic Island", "48MP Main Camera", "A16 Bionic Chip", "Ceramic Shield", "USB-C charging"]
    },
    {
        "id": "MOB-SAMS-S24",
        "title": "Samsung Galaxy S24 5G (Onyx Black, 256 GB)",
        "brand": "Samsung",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 74999.0,
        "original_price": 84999.0,
        "discount_pct": 11.8,
        "rating": 4.5,
        "rating_count": 14200,
        "stock": 38,
        "cost_price": 62000.0,
        "monthly_sales_units": 890,
        "image_url": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=600&auto=format&fit=crop&q=80",
        "description": "Galaxy AI is here. Circle to Search with Google, Live Translate on calls, Note Assist, and powerful 50MP ProVisual Engine with Armor Aluminum frame.",
        "specs": {
            "RAM": "8 GB",
            "Storage": "256 GB",
            "Processor": "Exynos 2400 Deca-Core",
            "Display": "6.2 inch Dynamic AMOLED 2X 120Hz",
            "Rear Camera": "50MP + 10MP (3x) + 12MP",
            "Front Camera": "12MP",
            "Battery": "4000 mAh (25W fast charging)",
            "5G": "Yes",
            "OS": "Android 14, One UI 6.1"
        },
        "features": ["Galaxy AI Suite", "Dynamic AMOLED 2X 2600 nits", "3x Optical Zoom", "IP68 Water Resistance"]
    },
    {
        "id": "MOB-ONEP-12R",
        "title": "OnePlus 12R (Cool Blue, 256 GB, 16 GB RAM)",
        "brand": "OnePlus",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 42999.0,
        "original_price": 45999.0,
        "discount_pct": 6.5,
        "rating": 4.6,
        "rating_count": 31900,
        "stock": 80,
        "cost_price": 36500.0,
        "monthly_sales_units": 2400,
        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=600&auto=format&fit=crop&q=80",
        "description": "Performance powerhouse powered by Snapdragon 8 Gen 2, monstrous 5500 mAh battery, and 100W SUPERVOOC charging.",
        "specs": {
            "RAM": "16 GB LPDDR5X",
            "Storage": "256 GB UFS 3.1",
            "Processor": "Snapdragon 8 Gen 2",
            "Display": "6.78 inch 1.5K ProXDR 120Hz LTPO4",
            "Rear Camera": "50MP Sony IMX890 OIS + 8MP + 2MP",
            "Front Camera": "16MP",
            "Battery": "5500 mAh (100W charging)",
            "5G": "Yes",
            "OS": "OxygenOS 14"
        },
        "features": ["100W SUPERVOOC charging in 26 mins", "5500 mAh Battery", "Snapdragon 8 Gen 2", "Aqua Touch"]
    },
    {
        "id": "MOB-REAL-12P",
        "title": "realme 12 Pro+ 5G (Submarine Blue, 256 GB)",
        "brand": "realme",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 28999.0,
        "original_price": 34999.0,
        "discount_pct": 17.1,
        "rating": 4.4,
        "rating_count": 48200,
        "stock": 110,
        "cost_price": 24000.0,
        "monthly_sales_units": 3100,
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600&auto=format&fit=crop&q=80",
        "description": "Periscope Portrait camera with 64MP sensor, Luxury Watch design, 120Hz Curved Vision Display and Snapdragon 7s Gen 2.",
        "specs": {
            "RAM": "8 GB",
            "Storage": "256 GB",
            "Processor": "Snapdragon 7s Gen 2",
            "Display": "6.7 inch Curved FHD+ OLED 120Hz",
            "Rear Camera": "64MP Periscope OIS + 50MP Sony IMX890 + 8MP",
            "Front Camera": "32MP Sony",
            "Battery": "5000 mAh (67W SUPERVOOC)",
            "5G": "Yes",
            "OS": "realme UI 5.0"
        },
        "features": ["64MP Periscope 3x-120x SuperZoom", "Luxury Vegan Leather", "120Hz Curved AMOLED"]
    },
    {
        "id": "MOB-MOTO-G84",
        "title": "Motorola Edge 50 Fusion (Marshmallow Blue, 256 GB)",
        "brand": "Motorola",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 22999.0,
        "original_price": 25999.0,
        "discount_pct": 11.5,
        "rating": 4.5,
        "rating_count": 52100,
        "stock": 95,
        "cost_price": 19000.0,
        "monthly_sales_units": 3800,
        "image_url": "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=600&auto=format&fit=crop&q=80",
        "description": "Segment best 50MP Sony LYTIA 700C OIS camera, IP68 underwater protection, 144Hz 3D curved pOLED display.",
        "specs": {
            "RAM": "12 GB",
            "Storage": "256 GB",
            "Processor": "Snapdragon 7s Gen 2",
            "Display": "6.7 inch 144Hz Endless Edge pOLED",
            "Rear Camera": "50MP Sony LYT-700C OIS + 13MP Ultrawide/Macro",
            "Front Camera": "32MP 4K selfie",
            "Battery": "5000 mAh (68W TurboPower)",
            "5G": "Yes",
            "OS": "Hello UI (Android 14)"
        },
        "features": ["IP68 Underwater Protection", "Sony LYTIA 700C Camera", "144Hz curved display", "Clean Android"]
    },
    {
        "id": "MOB-POCO-X6P",
        "title": "POCO X6 Pro 5G (Racing Yellow, 256 GB, 8 GB RAM)",
        "brand": "POCO",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 24999.0,
        "original_price": 30999.0,
        "discount_pct": 19.4,
        "rating": 4.4,
        "rating_count": 39800,
        "stock": 70,
        "cost_price": 20800.0,
        "monthly_sales_units": 2900,
        "image_url": "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=600&auto=format&fit=crop&q=80",
        "description": "AnTuTu 1.4 Million monster with Dimensity 8300-Ultra, 1.5K 120Hz AMOLED, and 64MP OIS triple camera.",
        "specs": {
            "RAM": "8 GB LPDDR5X",
            "Storage": "256 GB UFS 4.0",
            "Processor": "MediaTek Dimensity 8300-Ultra",
            "Display": "6.67 inch 1.5K CrystalRes Flow AMOLED 120Hz",
            "Rear Camera": "64MP OIS + 8MP + 2MP",
            "Front Camera": "16MP",
            "Battery": "5000 mAh (67W Turbo)",
            "5G": "Yes",
            "OS": "Xiaomi HyperOS"
        },
        "features": ["Dimensity 8300-Ultra Flagship Power", "WildBoost Gaming Optimization", "1800 nits Peak Display"]
    },
    {
        "id": "MOB-SAMS-M34",
        "title": "Samsung Galaxy M34 5G (Prism Silver, 128 GB)",
        "brand": "Samsung",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 14999.0,
        "original_price": 24499.0,
        "discount_pct": 38.8,
        "rating": 4.2,
        "rating_count": 78200,
        "stock": 140,
        "cost_price": 12500.0,
        "monthly_sales_units": 4500,
        "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=600&auto=format&fit=crop&q=80",
        "description": "Monster 6000 mAh battery with 50MP No Shake Cam (OIS) and 120Hz sAMOLED display with 4 OS upgrades promised.",
        "specs": {
            "RAM": "6 GB",
            "Storage": "128 GB",
            "Processor": "Exynos 1280 Octa-Core",
            "Display": "6.5 inch FHD+ 120Hz Super AMOLED",
            "Rear Camera": "50MP OIS + 8MP + 2MP",
            "Front Camera": "13MP",
            "Battery": "6000 mAh (25W supported)",
            "5G": "Yes",
            "OS": "Android 13, upgradable"
        },
        "features": ["6000 mAh Monster Battery", "50MP No Shake OIS Camera", "Super AMOLED 120Hz"]
    },
    {
        "id": "MOB-REDM-13C",
        "title": "REDMI 13C 5G (Starlight Green, 128 GB, 4 GB RAM)",
        "brand": "REDMI",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 9999.0,
        "original_price": 13999.0,
        "discount_pct": 28.6,
        "rating": 4.1,
        "rating_count": 94300,
        "stock": 210,
        "cost_price": 8400.0,
        "monthly_sales_units": 6100,
        "image_url": "https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=600&auto=format&fit=crop&q=80",
        "description": "Affordable 5G powerhouse with MediaTek Dimensity 6100+, 50MP AI dual camera, and 90Hz smooth display.",
        "specs": {
            "RAM": "4 GB",
            "Storage": "128 GB",
            "Processor": "Dimensity 6100+ 5G",
            "Display": "6.74 inch HD+ 90Hz Gorilla Glass",
            "Rear Camera": "50MP AI Dual Camera",
            "Front Camera": "5MP",
            "Battery": "5000 mAh (18W)",
            "5G": "Yes",
            "OS": "MIUI 14 based on Android 13"
        },
        "features": ["5G Dual SIM", "90Hz Smooth Display", "Corning Gorilla Glass", "Star Trail Design"]
    },

    # --- LAPTOPS ---
    {
        "id": "LAP-APPL-M2",
        "title": "Apple MacBook Air M2 (Midnight, 8 GB RAM, 256 GB SSD)",
        "brand": "Apple",
        "category": "Laptops",
        "sub_category": "Thin and Light",
        "price": 84990.0,
        "original_price": 99900.0,
        "discount_pct": 14.9,
        "rating": 4.7,
        "rating_count": 18500,
        "stock": 25,
        "cost_price": 72000.0,
        "monthly_sales_units": 650,
        "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600&auto=format&fit=crop&q=80",
        "description": "Strikingly thin design with M2 chip, 13.6-inch Liquid Retina display, MagSafe 3 charging, 1080p FaceTime HD camera, and up to 18 hours battery life.",
        "specs": {
            "Processor": "Apple M2 (8-core CPU, 8-core GPU)",
            "RAM": "8 GB Unified",
            "Storage": "256 GB SSD",
            "Display": "13.6 inch Liquid Retina True Tone 500 nits",
            "Weight": "1.24 kg",
            "Battery Life": "Up to 18 Hours",
            "OS": "macOS Sonoma"
        },
        "features": ["MagSafe 3 Charging", "Fanless Silent Operation", "Liquid Retina Display", "1.24kg Ultra Portable"]
    },
    {
        "id": "LAP-DELL-XPS13",
        "title": "DELL XPS 13 Core Ultra 7 (Platinum Silver, 16 GB, 512 GB SSD)",
        "brand": "DELL",
        "category": "Laptops",
        "sub_category": "Premium Ultrabook",
        "price": 129990.0,
        "original_price": 149990.0,
        "discount_pct": 13.3,
        "rating": 4.5,
        "rating_count": 3200,
        "stock": 15,
        "cost_price": 110000.0,
        "monthly_sales_units": 180,
        "image_url": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop&q=80",
        "description": "Iconic minimalist design crafted with CNC aluminum and Gorilla Glass 3. Powered by Intel Core Ultra 7 with dedicated NPU for AI.",
        "specs": {
            "Processor": "Intel Core Ultra 7 155H",
            "RAM": "16 GB LPDDR5X",
            "Storage": "512 GB PCIe 4.0 NVMe SSD",
            "Display": "13.4 inch FHD+ InfinityEdge 500 nits 120Hz",
            "Weight": "1.19 kg",
            "Battery Life": "Up to 14 Hours",
            "OS": "Windows 11 Home + MS Office"
        },
        "features": ["Seamless Glass Touchpad", "Capacitive Function Row", "Intel Evo Edition", "1.19kg CNC Chassis"]
    },
    {
        "id": "LAP-ASUS-G14",
        "title": "ASUS ROG Zephyrus G14 (Eclipse Gray, RTX 4060, Ryzen 9, 16 GB, 1 TB SSD)",
        "brand": "ASUS",
        "category": "Laptops",
        "sub_category": "Gaming Laptop",
        "price": 144990.0,
        "original_price": 169990.0,
        "discount_pct": 14.7,
        "rating": 4.8,
        "rating_count": 4100,
        "stock": 18,
        "cost_price": 122000.0,
        "monthly_sales_units": 310,
        "image_url": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80",
        "description": "Premium CNC aluminum gaming masterpiece featuring 3K 120Hz OLED ROG Nebula display, AMD Ryzen 9 8945HS, and NVIDIA GeForce RTX 4060.",
        "specs": {
            "Processor": "AMD Ryzen 9 8945HS (AI NPU included)",
            "RAM": "16 GB LPDDR5X",
            "Storage": "1 TB PCIe 4.0 NVMe SSD",
            "Graphics": "NVIDIA GeForce RTX 4060 8GB GDDR6 (90W TGP)",
            "Display": "14 inch 3K OLED 120Hz 0.2ms 500 nits",
            "Weight": "1.50 kg",
            "OS": "Windows 11 Home"
        },
        "features": ["3K 120Hz OLED Display", "Slash Lighting Lid", "Vapor Chamber Cooling", "1.5kg Thin & Light Gaming"]
    },
    {
        "id": "LAP-LENO-LOQ",
        "title": "Lenovo LOQ Intel Core i5 12th Gen (16 GB RAM, 512 GB SSD, RTX 3050 6GB)",
        "brand": "Lenovo",
        "category": "Laptops",
        "sub_category": "Gaming Laptop",
        "price": 61990.0,
        "original_price": 79990.0,
        "discount_pct": 22.5,
        "rating": 4.4,
        "rating_count": 21300,
        "stock": 55,
        "cost_price": 52000.0,
        "monthly_sales_units": 1450,
        "image_url": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=600&auto=format&fit=crop&q=80",
        "description": "Best value gaming laptop with 144Hz 100% sRGB display, RTX 3050 6GB with 95W TGP, and Lenovo LA1 AI chip tuning.",
        "specs": {
            "Processor": "Intel Core i5-12450HX (12-Threads)",
            "RAM": "16 GB DDR5 4800MHz (expandable)",
            "Storage": "512 GB SSD M.2 NVMe",
            "Graphics": "NVIDIA GeForce RTX 3050 6GB (95W TGP)",
            "Display": "15.6 inch FHD IPS 144Hz 300 nits 100% sRGB",
            "Weight": "2.38 kg",
            "OS": "Windows 11 Home"
        },
        "features": ["100% sRGB 144Hz Display", "95W TGP RTX 3050 6GB", "LA1 AI Engine for FPS Boost", "Fast Charge Pro"]
    },
    {
        "id": "LAP-HP-15S",
        "title": "HP 15s Intel Core i3 12th Gen (8 GB RAM, 512 GB SSD, Thin & Light)",
        "brand": "HP",
        "category": "Laptops",
        "sub_category": "Everyday / Student",
        "price": 36990.0,
        "original_price": 49990.0,
        "discount_pct": 26.0,
        "rating": 4.2,
        "rating_count": 44800,
        "stock": 120,
        "cost_price": 31000.0,
        "monthly_sales_units": 2900,
        "image_url": "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=600&auto=format&fit=crop&q=80",
        "description": "Dependable daily driver for students and office tasks with long-lasting battery life, micro-edge anti-glare display, and MS Office 2021 lifetime license.",
        "specs": {
            "Processor": "Intel Core i3-1215U (6 Cores, 8 Threads)",
            "RAM": "8 GB DDR4",
            "Storage": "512 GB PCIe NVMe M.2 SSD",
            "Display": "15.6 inch FHD Micro-Edge 250 nits",
            "Weight": "1.69 kg",
            "Battery Life": "Up to 7.5 Hours",
            "OS": "Windows 11 Home + MS Office 2021"
        },
        "features": ["Pre-installed MS Office Home & Student", "HP Fast Charge (50% in 45m)", "Numeric Keypad"]
    },

    # --- AUDIO & WEARABLES ---
    {
        "id": "AUD-SONY-1000XM5",
        "title": "Sony WH-1000XM5 Wireless Active Noise Cancelling Headphones (Silver)",
        "brand": "Sony",
        "category": "Audio",
        "sub_category": "Over-Ear Headphones",
        "price": 26990.0,
        "original_price": 34990.0,
        "discount_pct": 22.9,
        "rating": 4.7,
        "rating_count": 16700,
        "stock": 35,
        "cost_price": 21000.0,
        "monthly_sales_units": 720,
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&auto=format&fit=crop&q=80",
        "description": "Industry leading noise cancellation with two processors and 8 microphones. Hi-Res audio with LDAC, 30-hour battery, and Speak-to-Chat.",
        "specs": {
            "Type": "Over-Ear Wireless",
            "Driver": "30mm Carbon fiber composite",
            "Battery": "Up to 30 hours (with ANC)",
            "Bluetooth": "v5.2 (LDAC, AAC, SBC)",
            "Weight": "250 grams",
            "Multipoint": "Yes (connects to 2 devices)"
        },
        "features": ["Dual Processor V1 + QN1 ANC", "Speak-to-Chat & Quick Attention", "8 Beamforming Mics", "Ultra-comfortable soft fit leather"]
    },
    {
        "id": "AUD-BOAT-141",
        "title": "boAt Airdopes 141 Bluetooth Truly Wireless in Ear Earbuds (Bold Black)",
        "brand": "boAt",
        "category": "Audio",
        "sub_category": "TWS Earbuds",
        "price": 1099.0,
        "original_price": 4490.0,
        "discount_pct": 75.5,
        "rating": 4.0,
        "rating_count": 389000,
        "stock": 350,
        "cost_price": 680.0,
        "monthly_sales_units": 18500,
        "image_url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=600&auto=format&fit=crop&q=80",
        "description": "India's highest selling TWS earbuds with up to 42 hours total playback, ENx environmental noise cancellation for calls, and low latency beast mode.",
        "specs": {
            "Type": "In-Ear TWS",
            "Driver": "8mm boAt Signature Sound",
            "Battery": "Up to 42 hours total with case",
            "Fast Charging": "ASAP Charge (5 mins = 75 mins playtime)",
            "Water Resistance": "IPX4",
            "Latency": "80ms Beast Mode"
        },
        "features": ["42 Hours Playtime", "ENx Technology for Clear Calls", "Instant Wake 'N' Pair (IWP)", "ASAP Fast Charge"]
    },
    {
        "id": "AUD-APPL-APP2",
        "title": "Apple AirPods Pro (2nd Gen) with USB-C MagSafe Case",
        "brand": "Apple",
        "category": "Audio",
        "sub_category": "TWS Earbuds",
        "price": 20999.0,
        "original_price": 24900.0,
        "discount_pct": 15.7,
        "rating": 4.8,
        "rating_count": 29400,
        "stock": 40,
        "cost_price": 17500.0,
        "monthly_sales_units": 1100,
        "image_url": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=600&auto=format&fit=crop&q=80",
        "description": "Up to 2x more Active Noise Cancellation, Adaptive Audio, Transparency mode, and Personalized Spatial Audio with dynamic head tracking.",
        "specs": {
            "Chip": "Apple H2 headphone chip, U1 chip in case",
            "Battery": "Up to 6 hours listening (30 hours with case)",
            "Case": "USB-C MagSafe with Speaker and Lanyard loop",
            "Resistance": "IP54 Dust, sweat and water resistant"
        },
        "features": ["H2 Chip Audio Quality", "Adaptive Audio & Conversation Awareness", "Precision Finding with Find My", "Touch Control"]
    },
    {
        "id": "WEAR-SAMS-GW6",
        "title": "Samsung Galaxy Watch 6 LTE (44mm, Graphite)",
        "brand": "Samsung",
        "category": "Wearables",
        "sub_category": "Smartwatch",
        "price": 24999.0,
        "original_price": 36999.0,
        "discount_pct": 32.4,
        "rating": 4.4,
        "rating_count": 8900,
        "stock": 30,
        "cost_price": 19500.0,
        "monthly_sales_units": 450,
        "image_url": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=600&auto=format&fit=crop&q=80",
        "description": "20% larger display, advanced sleep coaching, ECG and blood pressure monitoring, BIA body composition sensor, and standalone 4G LTE calls.",
        "specs": {
            "Display": "1.5 inch Super AMOLED Sapphire Crystal (480x480)",
            "Connectivity": "LTE 4G eSIM, Bluetooth 5.3, Wi-Fi, NFC",
            "Sensors": "BioActive Sensor (Optical Heart + ECG + BIA)",
            "Durability": "5ATM + IP68 / MIL-STD-810H",
            "Battery": "425 mAh (WPC wireless fast charge)"
        },
        "features": ["Standalone LTE Calling", "Advanced Sleep Coaching", "Body Composition Analysis (BIA)", "Sapphire Crystal Glass"]
    },
    {
        "id": "WEAR-NOIS-COLOR",
        "title": "Noise ColorFit Pulse 3 Smartwatch (Jet Black, 1.96-inch TFT)",
        "brand": "Noise",
        "category": "Wearables",
        "sub_category": "Smartwatch",
        "price": 1499.0,
        "original_price": 4999.0,
        "discount_pct": 70.0,
        "rating": 4.1,
        "rating_count": 128000,
        "stock": 280,
        "cost_price": 950.0,
        "monthly_sales_units": 9200,
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80",
        "description": "Massive 1.96-inch display, Bluetooth calling with Tru Sync technology, 100+ sports modes, and up to 7-day battery life.",
        "specs": {
            "Display": "1.96 inch TFT 550 nits (240x282)",
            "Battery": "Up to 7 days normal use (2 days with BT calling)",
            "Calling": "Bluetooth v5.3 Tru Sync Calling",
            "Waterproof": "IP68 water resistant"
        },
        "features": ["1.96-inch HD Display", "Advanced Bluetooth Calling", "Auto Sport Detection", "Noise Health Suite (SpO2, 24x7 Heart Rate)"]
    },

    # --- HOME APPLIANCES & TVS ---
    {
        "id": "HOME-LG-55OLED",
        "title": "LG 55-inch 4K Ultra HD Smart OLED evo TV (OLED55C3PSA)",
        "brand": "LG",
        "category": "Appliances",
        "sub_category": "Smart TVs",
        "price": 114990.0,
        "original_price": 174990.0,
        "discount_pct": 34.3,
        "rating": 4.8,
        "rating_count": 6200,
        "stock": 20,
        "cost_price": 94000.0,
        "monthly_sales_units": 240,
        "image_url": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=600&auto=format&fit=crop&q=80",
        "description": "Infinite contrast with self-lit OLED pixels, Brightness Booster, α9 AI Processor 4K Gen6, Dolby Vision IQ & Dolby Atmos, and 0.1ms 120Hz 4K gaming.",
        "specs": {
            "Display": "55 inch 4K OLED (3840x2160) 120Hz",
            "Processor": "α9 AI Processor 4K Gen6",
            "Audio": "40W 2.2 Channel Dolby Atmos",
            "Ports": "4 x HDMI 2.1 (4K 120Hz, eARC, VRR, ALLM)",
            "Smart OS": "webOS 23 with Magic Remote"
        },
        "features": ["Self-lit OLED evo Pixels", "NVIDIA G-Sync & AMD FreeSync Premium", "Dolby Vision & Dolby Atmos", "Hands-free Voice Control"]
    },
    {
        "id": "HOME-MI-43X",
        "title": "Xiaomi X Series 43-inch 4K Ultra HD Smart Google TV",
        "brand": "Xiaomi",
        "category": "Appliances",
        "sub_category": "Smart TVs",
        "price": 24999.0,
        "original_price": 42999.0,
        "discount_pct": 41.9,
        "rating": 4.3,
        "rating_count": 71500,
        "stock": 85,
        "cost_price": 20500.0,
        "monthly_sales_units": 3400,
        "image_url": "https://images.unsplash.com/photo-1461151304267-38535e780c79?w=600&auto=format&fit=crop&q=80",
        "description": "True 4K bezel-less display with Dolby Vision, 30W Dolby Audio stereo speakers, PatchWall+ with Google TV, and 2GB RAM + 8GB Storage.",
        "specs": {
            "Display": "43 inch 4K UHD (3840x2160) 60Hz Vivid Picture Engine",
            "Audio": "30W Stereo with Dolby Audio and DTS:X",
            "Ports": "3 x HDMI 2.1 (ALLM, eARC), 2 x USB",
            "OS": "Google TV with PatchWall+"
        },
        "features": ["Bezel-less Metal Design", "Dolby Vision & HDR10", "30W Cinematic Sound", "Google Assistant Built-in"]
    },
    {
        "id": "HOME-SAMS-REF",
        "title": "Samsung 236L Double Door Convertible Refrigerator (Elegant Inox)",
        "brand": "Samsung",
        "category": "Appliances",
        "sub_category": "Refrigerators",
        "price": 26990.0,
        "original_price": 37990.0,
        "discount_pct": 29.0,
        "rating": 4.4,
        "rating_count": 33100,
        "stock": 42,
        "cost_price": 22000.0,
        "monthly_sales_units": 980,
        "image_url": "https://images.unsplash.com/photo-1584992236310-6edddc08acff?w=600&auto=format&fit=crop&q=80",
        "description": "Digital Inverter 3 Star frost free double door refrigerator with convertible 2-in-1 mode, toughened glass shelves, and 20-year compressor warranty.",
        "specs": {
            "Capacity": "236 Litres (Freezer: 53L, Fridge: 183L)",
            "Energy Rating": "3 Star BEE",
            "Compressor": "Digital Inverter Technology (Quiet & Durable)",
            "Deodorizer": "Active Fresh Filter",
            "Warranty": "1 Year on Product, 20 Years on Compressor"
        },
        "features": ["Convertible 2-in-1 Freezer to Fridge", "Stabilizer Free Operation (100V - 300V)", "All Around Cooling"]
    },
    {
        "id": "HOME-LG-WASH",
        "title": "LG 8 Kg 5 Star AI Direct Drive Front Load Washing Machine",
        "brand": "LG",
        "category": "Appliances",
        "sub_category": "Washing Machines",
        "price": 37990.0,
        "original_price": 54990.0,
        "discount_pct": 30.9,
        "rating": 4.5,
        "rating_count": 24900,
        "stock": 35,
        "cost_price": 31000.0,
        "monthly_sales_units": 820,
        "image_url": "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=600&auto=format&fit=crop&q=80",
        "description": "AI DD technology detects weight and fabric softness to optimize wash motion. Steam wash removes 99.9% allergens, TurboWash 59 mins.",
        "specs": {
            "Capacity": "8.0 Kg (Ideal for families of 4-6)",
            "Motor": "Inverter Direct Drive (1400 RPM)",
            "Energy Rating": "5 Star 2024",
            "Connectivity": "LG ThinQ Wi-Fi",
            "Warranty": "2 Years comprehensive, 10 Years on Motor"
        },
        "features": ["AI DD Fabric Care", "Steam Allergy Care Cycle", "TurboWash in 59 mins", "6 Motion Direct Drive"]
    },

    # --- FASHION & LIFESTYLE ---
    {
        "id": "FASH-PUMA-SHOES",
        "title": "Puma Men Nitro Velocity 3 Running Shoes (Puma Black)",
        "brand": "Puma",
        "category": "Fashion",
        "sub_category": "Footwear",
        "price": 5999.0,
        "original_price": 10999.0,
        "discount_pct": 45.5,
        "rating": 4.5,
        "rating_count": 14200,
        "stock": 65,
        "cost_price": 3400.0,
        "monthly_sales_units": 1800,
        "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80",
        "description": "Advanced nitrogen-injected foam delivers superior responsiveness and cushioning in a lightweight package. PUMAGRIP durable rubber outsole.",
        "specs": {
            "Cushioning": "NITRO Foam technology",
            "Sole": "PUMAGRIP rubber traction",
            "Upper": "Engineered breathable mesh",
            "Drop": "8mm",
            "Weight": "260 grams"
        },
        "features": ["NITRO Foam Cushioning", "PUMAGRIP All-surface Traction", "Reflective accents for low light"]
    },
    {
        "id": "FASH-LEVIS-511",
        "title": "Levi's Men 511 Slim Fit Mid Rise Stretch Jeans (Dark Indigo)",
        "brand": "Levi's",
        "category": "Fashion",
        "sub_category": "Men's Clothing",
        "price": 2199.0,
        "original_price": 3999.0,
        "discount_pct": 45.0,
        "rating": 4.3,
        "rating_count": 31200,
        "stock": 190,
        "cost_price": 1300.0,
        "monthly_sales_units": 4200,
        "image_url": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600&auto=format&fit=crop&q=80",
        "description": "The quintessential slim jean cut close to the body with added stretch for all-day comfort, crafted from premium sustainable cotton blend.",
        "specs": {
            "Fit": "Slim Fit, sits below waist",
            "Fabric": "98% Cotton, 2% Elastane",
            "Wash": "Machine cold wash",
            "Closure": "Zip fly with button closure"
        },
        "features": ["Levi's Flex Comfort Stretch", "Iconic Arcuate Back Pocket Stitching", "Classic 5-pocket styling"]
    }
]

# Competitor benchmarks for price intelligence
SAMPLE_COMPETITORS = [
    {"product_id": "MOB-APPL-IP15", "competitor_name": "Amazon", "price": 66499.0, "in_stock": True, "delivery_days": 1},
    {"product_id": "MOB-APPL-IP15", "competitor_name": "Croma", "price": 66990.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "MOB-APPL-IP15", "competitor_name": "Reliance Digital", "price": 67490.0, "in_stock": True, "delivery_days": 2},

    {"product_id": "MOB-SAMS-S24", "competitor_name": "Amazon", "price": 74499.0, "in_stock": True, "delivery_days": 1},
    {"product_id": "MOB-SAMS-S24", "competitor_name": "Croma", "price": 75999.0, "in_stock": True, "delivery_days": 3},
    {"product_id": "MOB-SAMS-S24", "competitor_name": "Reliance Digital", "price": 74999.0, "in_stock": False, "delivery_days": 5},

    {"product_id": "MOB-ONEP-12R", "competitor_name": "Amazon", "price": 42999.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "MOB-ONEP-12R", "competitor_name": "Croma", "price": 43499.0, "in_stock": True, "delivery_days": 2},

    {"product_id": "MOB-REAL-12P", "competitor_name": "Amazon", "price": 29499.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "MOB-REAL-12P", "competitor_name": "Reliance Digital", "price": 29999.0, "in_stock": True, "delivery_days": 3},

    {"product_id": "MOB-MOTO-G84", "competitor_name": "Amazon", "price": 23499.0, "in_stock": True, "delivery_days": 3},
    {"product_id": "MOB-POCO-X6P", "competitor_name": "Amazon", "price": 25499.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "MOB-SAMS-M34", "competitor_name": "Amazon", "price": 15499.0, "in_stock": True, "delivery_days": 1},
    {"product_id": "MOB-REDM-13C", "competitor_name": "Amazon", "price": 10499.0, "in_stock": True, "delivery_days": 2},

    {"product_id": "LAP-APPL-M2", "competitor_name": "Amazon", "price": 85990.0, "in_stock": True, "delivery_days": 1},
    {"product_id": "LAP-APPL-M2", "competitor_name": "Croma", "price": 86900.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "LAP-DELL-XPS13", "competitor_name": "Amazon", "price": 134990.0, "in_stock": True, "delivery_days": 3},
    {"product_id": "LAP-ASUS-G14", "competitor_name": "Amazon", "price": 147990.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "LAP-LENO-LOQ", "competitor_name": "Amazon", "price": 63990.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "LAP-HP-15S", "competitor_name": "Amazon", "price": 37490.0, "in_stock": True, "delivery_days": 2},

    {"product_id": "AUD-SONY-1000XM5", "competitor_name": "Amazon", "price": 26990.0, "in_stock": True, "delivery_days": 1},
    {"product_id": "AUD-SONY-1000XM5", "competitor_name": "Croma", "price": 27990.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "AUD-BOAT-141", "competitor_name": "Amazon", "price": 1199.0, "in_stock": True, "delivery_days": 1},
    {"product_id": "AUD-APPL-APP2", "competitor_name": "Amazon", "price": 21499.0, "in_stock": True, "delivery_days": 1},
    {"product_id": "WEAR-SAMS-GW6", "competitor_name": "Amazon", "price": 25499.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "WEAR-NOIS-COLOR", "competitor_name": "Amazon", "price": 1599.0, "in_stock": True, "delivery_days": 1},

    {"product_id": "HOME-LG-55OLED", "competitor_name": "Amazon", "price": 118990.0, "in_stock": True, "delivery_days": 3},
    {"product_id": "HOME-LG-55OLED", "competitor_name": "Croma", "price": 119990.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "HOME-MI-43X", "competitor_name": "Amazon", "price": 25999.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "HOME-SAMS-REF", "competitor_name": "Amazon", "price": 27490.0, "in_stock": True, "delivery_days": 3},
    {"product_id": "HOME-LG-WASH", "competitor_name": "Amazon", "price": 38490.0, "in_stock": True, "delivery_days": 3},
    {"product_id": "FASH-PUMA-SHOES", "competitor_name": "Amazon", "price": 6299.0, "in_stock": True, "delivery_days": 2},
    {"product_id": "FASH-LEVIS-511", "competitor_name": "Amazon", "price": 2399.0, "in_stock": True, "delivery_days": 2}
]

# Detailed aspect-tagged reviews for RAG & Sentiment Analytics
SAMPLE_REVIEWS = [
    # iPhone 15
    {
        "product_id": "MOB-APPL-IP15",
        "author": "Rahul Sharma",
        "rating": 5.0,
        "title": "Stunning camera upgrade and USB-C is a lifesaver!",
        "review_text": "Upgraded from iPhone 11 and the difference is night and day. The 48MP camera takes mindblowing photos in daylight and low-light. The Dynamic Island is genuinely handy. Battery life comfortably lasts a full day of moderate-heavy usage. Value for money during Flipkart sale!",
        "aspects": {"Camera": 1.0, "Battery": 0.8, "Build": 1.0, "Value for Money": 0.9, "Delivery": 1.0},
        "verified_purchase": True,
        "helpful_count": 342,
        "created_at": "2025-02-10"
    },
    {
        "product_id": "MOB-APPL-IP15",
        "author": "Priya V.",
        "rating": 4.0,
        "title": "Great phone, but still 60Hz display at this price",
        "review_text": "Everything about the iPhone 15 feels premium. The matte back glass feels luxurious and light in hand. iOS 17 is buttery smooth. However, Apple really should give 120Hz ProMotion at this price point. Fast charging speed caps around 20W which is slower than Android competitors.",
        "aspects": {"Display": -0.4, "Performance": 0.9, "Build": 1.0, "Battery": 0.4, "Value for Money": 0.2},
        "verified_purchase": True,
        "helpful_count": 189,
        "created_at": "2025-01-28"
    },
    {
        "product_id": "MOB-APPL-IP15",
        "author": "Karthik R.",
        "rating": 5.0,
        "title": "Superb Flipkart delivery and authentic unit",
        "review_text": "Ordered during the Big Billion Days and received within 24 hours with Open Box delivery. The camera portraits have natural bokeh, battery lasts 7+ hours screen-on-time.",
        "aspects": {"Delivery": 1.0, "Camera": 1.0, "Battery": 0.9},
        "verified_purchase": True,
        "helpful_count": 92,
        "created_at": "2025-01-14"
    },

    # Samsung S24
    {
        "product_id": "MOB-SAMS-S24",
        "author": "Amit Sengupta",
        "rating": 5.0,
        "title": "Galaxy AI features are futuristic and display is breathtaking",
        "review_text": "The flat 120Hz Dynamic AMOLED display is arguably the best on the market, incredibly bright outdoors. Galaxy AI features like Circle to Search and Live Call Translation are genuinely useful in my daily corporate routine. Camera colors are punchy and 3x optical zoom is crisp.",
        "aspects": {"Display": 1.0, "Performance": 0.9, "Camera": 0.9, "Build": 0.9},
        "verified_purchase": True,
        "helpful_count": 210,
        "created_at": "2025-02-04"
    },
    {
        "product_id": "MOB-SAMS-S24",
        "author": "Deepak Mehta",
        "rating": 3.0,
        "title": "Exynos heats up during heavy gaming, battery is average",
        "review_text": "The phone is compact and looks gorgeous. But when playing BGMI or Genshin Impact for over 30 minutes, it gets warm and thermal throttles. The 4000 mAh battery requires a mid-day top-up if you are a heavy user.",
        "aspects": {"Performance": -0.6, "Battery": -0.7, "Build": 0.8, "Value for Money": -0.3},
        "verified_purchase": True,
        "helpful_count": 154,
        "created_at": "2025-01-18"
    },

    # OnePlus 12R
    {
        "product_id": "MOB-ONEP-12R",
        "author": "Vikram Rathore",
        "rating": 5.0,
        "title": "Unmatched value under 45k! Battery and charging speed are beasts",
        "review_text": "The Snapdragon 8 Gen 2 delivers flagship grade gaming without heating. The 5500 mAh battery easily lasts 1.5 to 2 days, and the 100W charger juices it in under 28 minutes. Screen is gorgeous with LTPO4 smooth scrolling.",
        "aspects": {"Performance": 1.0, "Battery": 1.0, "Value for Money": 1.0, "Display": 0.9},
        "verified_purchase": True,
        "helpful_count": 420,
        "created_at": "2025-02-12"
    },
    {
        "product_id": "MOB-ONEP-12R",
        "author": "Sneha Nair",
        "rating": 4.0,
        "title": "Great performance, average macro and ultrawide camera",
        "review_text": "Main 50MP Sony camera takes sharp photos, but the 8MP ultrawide and 2MP macro cameras are just ordinary filler lenses. If camera is your #1 priority, look at Pixel or Vivo. For everything else, OnePlus 12R is undefeated.",
        "aspects": {"Camera": 0.1, "Performance": 0.9, "Battery": 1.0, "Value for Money": 0.8},
        "verified_purchase": True,
        "helpful_count": 178,
        "created_at": "2025-01-22"
    },

    # realme 12 Pro+
    {
        "product_id": "MOB-REAL-12P",
        "author": "Tanmay Deshmukh",
        "rating": 5.0,
        "title": "Periscope portrait camera under 30k is unbelievable!",
        "review_text": "The 64MP periscope telephoto lens takes DSLR-like portrait shots with authentic background blur and 3x optical reach. Luxury watch design on the back turns heads everywhere. Fast 67W charging and snappy curved display.",
        "aspects": {"Camera": 1.0, "Build": 1.0, "Value for Money": 1.0, "Battery": 0.7},
        "verified_purchase": True,
        "helpful_count": 284,
        "created_at": "2025-02-08"
    },

    # Motorola Edge 50 Fusion
    {
        "product_id": "MOB-MOTO-G84",
        "author": "Arun Prakash",
        "rating": 5.0,
        "title": "Best clean UI and waterproof phone in segment",
        "review_text": "Zero bloatware, clean stock Android experience with Moto gestures. IP68 underwater rating at 23k is a game changer. The curved 144Hz pOLED screen looks flagship. Battery gives 7 hours SOT.",
        "aspects": {"Performance": 0.8, "Build": 1.0, "Display": 1.0, "Value for Money": 1.0, "Battery": 0.8},
        "verified_purchase": True,
        "helpful_count": 312,
        "created_at": "2025-02-14"
    },

    # POCO X6 Pro
    {
        "product_id": "MOB-POCO-X6P",
        "author": "Rohan Joshi",
        "rating": 5.0,
        "title": "Pure gaming monster on a budget",
        "review_text": "Dimensity 8300 Ultra blows every benchmark away at this price point. 120 FPS gaming is fluid. The 1.5K display is crisp with tiny bezels. Battery lasts a day with fast 67W charging.",
        "aspects": {"Performance": 1.0, "Display": 0.9, "Value for Money": 1.0, "Battery": 0.6},
        "verified_purchase": True,
        "helpful_count": 290,
        "created_at": "2025-01-30"
    },

    # MacBook Air M2
    {
        "product_id": "LAP-APPL-M2",
        "author": "Sunil Verma",
        "rating": 5.0,
        "title": "The ultimate coding & productivity laptop",
        "review_text": "Battery life is simply ridiculous — I code for 14 hours straight on a single charge without carrying a brick. M2 chip is completely silent with no fan noise. Screen is vivid and keyboard is a joy. Best laptop purchase ever.",
        "aspects": {"Battery": 1.0, "Performance": 1.0, "Build": 1.0, "Display": 0.9, "Value for Money": 0.8},
        "verified_purchase": True,
        "helpful_count": 510,
        "created_at": "2025-02-01"
    },
    {
        "product_id": "LAP-APPL-M2",
        "author": "Divya Krishnan",
        "rating": 4.0,
        "title": "8GB unified memory can bottleneck heavy video rendering",
        "review_text": "For regular multitasking, browsing, office work and light photo editing, it flies. But if you open multiple 4K timelines or heavy Docker containers, 8GB memory pressure starts swap memory. Recommend 16GB if your budget permits.",
        "aspects": {"Performance": 0.4, "Battery": 1.0, "Build": 1.0, "Value for Money": 0.5},
        "verified_purchase": True,
        "helpful_count": 230,
        "created_at": "2025-01-12"
    },

    # ASUS Zephyrus G14
    {
        "product_id": "LAP-ASUS-G14",
        "author": "Varun Chawla",
        "rating": 5.0,
        "title": "Dream machine: OLED screen + RTX 4060 in 1.5kg body",
        "review_text": "The 3K OLED panel is breathtaking with infinite blacks and 120Hz refresh rate. Cyberpunk 2077 runs smoothly above 75 FPS with DLSS 3. Speakers sound rich, build quality matches MacBook, and battery lasts 7 hours in eco mode.",
        "aspects": {"Display": 1.0, "Performance": 1.0, "Build": 1.0, "Value for Money": 0.7, "Battery": 0.7},
        "verified_purchase": True,
        "helpful_count": 140,
        "created_at": "2025-01-20"
    },

    # Sony WH-1000XM5
    {
        "product_id": "AUD-SONY-1000XM5",
        "author": "Aakash Banerjee",
        "rating": 5.0,
        "title": "Silence on demand. ANC is unbeatable on flights and trains",
        "review_text": "The ANC completely erases flight drone and AC humming. LDAC codec delivers audiophile clarity on Tidal / Apple Music Lossless. Multipoint seamless switching between MacBook and phone. 30 hour battery means charging once every two weeks.",
        "aspects": {"Noise Cancellation": 1.0, "Battery": 1.0, "Sound Quality": 1.0, "Build": 0.8},
        "verified_purchase": True,
        "helpful_count": 380,
        "created_at": "2025-02-05"
    },

    # boAt Airdopes 141
    {
        "product_id": "AUD-BOAT-141",
        "author": "Manish Gupta",
        "rating": 4.0,
        "title": "Insane bass and crazy 42 hours battery for ₹1099!",
        "review_text": "For the price of a dinner, boAt delivers thumping bass that EDM and Punjabi music lovers will adore. Case battery lasts forever. Call quality outdoors is just passable in heavy traffic, but for gym and music it cannot be beaten.",
        "aspects": {"Value for Money": 1.0, "Battery": 1.0, "Sound Quality": 0.6, "Call Quality": 0.1},
        "verified_purchase": True,
        "helpful_count": 920,
        "created_at": "2025-01-25"
    },

    # Apple AirPods Pro 2
    {
        "product_id": "AUD-APPL-APP2",
        "author": "Meera Swaminathan",
        "rating": 5.0,
        "title": "Transparency mode feels like not wearing anything at all",
        "review_text": "Adaptive audio transitions flawlessly between ANC and Transparency. USB-C case is finally universal. Spatial Audio makes movies feel like a personal IMAX theatre. Essential for iPhone and Mac users.",
        "aspects": {"Sound Quality": 1.0, "Noise Cancellation": 1.0, "Build": 1.0, "Value for Money": 0.7},
        "verified_purchase": True,
        "helpful_count": 310,
        "created_at": "2025-02-11"
    },

    # LG OLED TV
    {
        "product_id": "HOME-LG-55OLED",
        "author": "Sanjay Narang",
        "rating": 5.0,
        "title": "Pure cinema in living room. Once you go OLED, you never go back",
        "review_text": "Perfect blacks, infinite contrast, and vibrant HDR highlights. PS5 gaming with 4K 120Hz VRR is silky smooth. WebOS is fluid with the pointer remote. Premium investment that transforms entertainment.",
        "aspects": {"Display": 1.0, "Performance": 1.0, "Build": 1.0, "Value for Money": 0.8},
        "verified_purchase": True,
        "helpful_count": 185,
        "created_at": "2025-01-09"
    },

    # Xiaomi X Series 43 TV
    {
        "product_id": "HOME-MI-43X",
        "author": "Pooja Hegde",
        "rating": 4.0,
        "title": "Best budget 4K TV for bedrooms and compact living rooms",
        "review_text": "Dolby Vision clarity at 25k is impressive. PatchWall makes discovering content across OTT platforms super easy. 30W speakers are loud and clear without soundbar. Minor UI stutter when opening heavy apps.",
        "aspects": {"Display": 0.8, "Sound Quality": 0.8, "Value for Money": 1.0, "Performance": 0.3},
        "verified_purchase": True,
        "helpful_count": 420,
        "created_at": "2025-01-19"
    },

    # Puma Nitro Velocity 3
    {
        "product_id": "FASH-PUMA-SHOES",
        "author": "Kishore Kumar",
        "rating": 5.0,
        "title": "Best daily trainer shoe. Super springy Nitro foam",
        "review_text": "Clocked over 150 km on tarmac and track. The cushioning protects knees on long 10k runs. PUMAGRIP has top-tier traction even on wet morning roads. Outstanding value compared to Pegasus or Ultraboost.",
        "aspects": {"Comfort": 1.0, "Build": 1.0, "Value for Money": 1.0},
        "verified_purchase": True,
        "helpful_count": 195,
        "created_at": "2025-02-03"
    }
]
