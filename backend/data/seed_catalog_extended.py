"""
Expands catalog and reviews to 50+ products and hundreds of aspect-annotated reviews.
"""
import random

ADDITIONAL_PRODUCTS = [
    # More Mobiles
    {
        "id": "MOB-VIVO-V30P",
        "title": "vivo V30 Pro 5G (Classic Black, 512 GB, 12 GB RAM)",
        "brand": "vivo",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 41999.0,
        "original_price": 46999.0,
        "discount_pct": 10.6,
        "rating": 4.5,
        "rating_count": 21000,
        "stock": 45,
        "cost_price": 35000.0,
        "monthly_sales_units": 1600,
        "image_url": "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=600&auto=format&fit=crop&q=80",
        "description": "Co-engineered with ZEISS. Studio quality portraits with ZEISS Style Portrait and Smart Aura Light. Slimmest 5000 mAh phone in the world.",
        "specs": {"RAM": "12 GB", "Storage": "512 GB", "Processor": "MediaTek Dimensity 8200", "Display": "6.78 inch 1.5K 120Hz 3D Curved AMOLED", "Rear Camera": "50MP ZEISS Sony IMX920 + 50MP Telephoto + 50MP Ultrawide", "Battery": "5000 mAh (80W FlashCharge)"},
        "features": ["ZEISS Professional Portrait Camera", "Studio Quality Aura Light", "1.5K 120Hz Curved AMOLED", "Slimmest 5000mAh Body"]
    },
    {
        "id": "MOB-PIX-8A",
        "title": "Google Pixel 8a (Bay Blue, 128 GB, 8 GB RAM)",
        "brand": "Google",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 49999.0,
        "original_price": 52999.0,
        "discount_pct": 5.6,
        "rating": 4.3,
        "rating_count": 9800,
        "stock": 35,
        "cost_price": 43000.0,
        "monthly_sales_units": 850,
        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=600&auto=format&fit=crop&q=80",
        "description": "Google AI inside with Tensor G3 chip. Best Take, Magic Editor, Audio Magic Eraser, and 7 years of guaranteed OS and security updates.",
        "specs": {"RAM": "8 GB", "Storage": "128 GB", "Processor": "Google Tensor G3 + Titan M2", "Display": "6.1 inch Actua OLED 120Hz", "Rear Camera": "64MP Quad PD + 13MP Ultrawide", "Battery": "4492 mAh"},
        "features": ["7 Years OS Updates", "Google AI Best Take & Magic Editor", "Actua 120Hz Display", "IP67 Water Resistance"]
    },
    {
        "id": "MOB-IQOO-12",
        "title": "iQOO 12 5G (Legend White BMW M Motorsport, 256 GB)",
        "brand": "iQOO",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 52999.0,
        "original_price": 59999.0,
        "discount_pct": 11.6,
        "rating": 4.6,
        "rating_count": 18400,
        "stock": 50,
        "cost_price": 45000.0,
        "monthly_sales_units": 1400,
        "image_url": "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=600&auto=format&fit=crop&q=80",
        "description": "India's first Snapdragon 8 Gen 3 flagship with Supercomputing Chip Q1. 144Hz LTPO AMOLED and 120W FlashCharge.",
        "specs": {"RAM": "12 GB LPDDR5X", "Storage": "256 GB UFS 4.0", "Processor": "Snapdragon 8 Gen 3", "Display": "6.78 inch 144Hz 1.5K LTPO AMOLED 3000 nits", "Rear Camera": "50MP 1/1.3\" + 50MP UW + 64MP 3x Periscope OIS", "Battery": "5000 mAh (120W Charge)"},
        "features": ["Snapdragon 8 Gen 3 + Q1 Chip", "144Hz LTPO Display", "64MP Periscope 100x Zoom", "120W Charger Included"]
    },
    {
        "id": "MOB-NOTH-2A",
        "title": "Nothing Phone (2a) 5G (White, 128 GB, 8 GB RAM)",
        "brand": "Nothing",
        "category": "Mobiles",
        "sub_category": "Smartphones",
        "price": 23999.0,
        "original_price": 25999.0,
        "discount_pct": 7.7,
        "rating": 4.4,
        "rating_count": 62000,
        "stock": 90,
        "cost_price": 20000.0,
        "monthly_sales_units": 3600,
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600&auto=format&fit=crop&q=80",
        "description": "Iconic transparent design with Glyph Interface. Powered by custom Dimensity 7200 Pro, 50MP dual cameras, and Nothing OS 2.5.",
        "specs": {"RAM": "8 GB", "Storage": "128 GB", "Processor": "Dimensity 7200 Pro 5G", "Display": "6.7 inch Flexible AMOLED 120Hz", "Rear Camera": "50MP OIS + 50MP Ultrawide", "Battery": "5000 mAh (45W Fast Charging)"},
        "features": ["Glyph Interface Lights", "Nothing OS 2.5 Clean Software", "50MP Dual OIS Cameras", "1300 nits Peak Brightness"]
    },

    # More Laptops
    {
        "id": "LAP-ACER-PRED",
        "title": "Acer Predator Helios Neo 16 Intel Core i7 14th Gen (16 GB, 1 TB SSD, RTX 4060)",
        "brand": "Acer",
        "category": "Laptops",
        "sub_category": "Gaming Laptop",
        "price": 119990.0,
        "original_price": 144990.0,
        "discount_pct": 17.2,
        "rating": 4.6,
        "rating_count": 5200,
        "stock": 22,
        "cost_price": 99000.0,
        "monthly_sales_units": 450,
        "image_url": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=600&auto=format&fit=crop&q=80",
        "description": "Extreme gaming power with Intel 14th Gen Core i7-14700HX, RTX 4060 140W TGP, 165Hz WQXGA IPS 100% sRGB display, and 5th Gen AeroBlade 3D fans.",
        "specs": {"Processor": "Intel Core i7-14700HX (20 Cores)", "RAM": "16 GB DDR5 5600MHz", "Storage": "1 TB PCIe Gen4 SSD", "Graphics": "RTX 4060 8GB GDDR6 (140W TGP)", "Display": "16 inch WQXGA (2560x1600) 165Hz 500 nits 100% sRGB", "Weight": "2.6 kg"},
        "features": ["140W Full TGP RTX 4060", "Liquid Metal Thermal Grease", "RGB 4-Zone Keyboard", "16:10 165Hz QHD+ Screen"]
    },
    {
        "id": "LAP-HP-VICTUS",
        "title": "HP Victus AMD Ryzen 5 Hexa Core 5600H (16 GB RAM, 512 GB SSD, RTX 3050 4GB)",
        "brand": "HP",
        "category": "Laptops",
        "sub_category": "Gaming Laptop",
        "price": 54990.0,
        "original_price": 69990.0,
        "discount_pct": 21.4,
        "rating": 4.3,
        "rating_count": 28900,
        "stock": 60,
        "cost_price": 46000.0,
        "monthly_sales_units": 1900,
        "image_url": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80",
        "description": "Superb 1080p gaming with AMD Ryzen 5 5600H, NVIDIA RTX 3050 4GB, upgraded cooling chamber, and fast B&O tuned dual speakers.",
        "specs": {"Processor": "AMD Ryzen 5 5600H (6 Cores, 12 Threads)", "RAM": "16 GB DDR4", "Storage": "512 GB PCIe NVMe M.2 SSD", "Graphics": "RTX 3050 4GB", "Display": "15.6 inch FHD IPS 144Hz 250 nits", "Weight": "2.37 kg"},
        "features": ["OMEN Gaming Hub Control", "Audio by Bang & Olufsen", "144Hz Anti-Glare Screen", "Fast Charge 50% in 30m"]
    },
    {
        "id": "LAP-ASUS-VIVO15",
        "title": "ASUS Vivobook 15 Intel Core i5 12th Gen (16 GB RAM, 512 GB SSD, Thin & Light)",
        "brand": "ASUS",
        "category": "Laptops",
        "sub_category": "Thin and Light",
        "price": 46990.0,
        "original_price": 62990.0,
        "discount_pct": 25.4,
        "rating": 4.3,
        "rating_count": 36400,
        "stock": 80,
        "cost_price": 39000.0,
        "monthly_sales_units": 2300,
        "image_url": "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=600&auto=format&fit=crop&q=80",
        "description": "Sleek metallic lid, 180-degree lay-flat hinge, physical webcam privacy shield, and ASUS Antimicrobial Guard Plus.",
        "specs": {"Processor": "Intel Core i5-1235U (10 Cores)", "RAM": "16 GB DDR4", "Storage": "512 GB M.2 NVMe SSD", "Display": "15.6 inch FHD NanoEdge 250 nits", "Weight": "1.70 kg", "OS": "Windows 11 Home + Office Home 2021"},
        "features": ["180-degree Lay-flat Hinge", "Webcam Privacy Shield", "ErgoSense Keyboard", "Antimicrobial Protection"]
    },
    {
        "id": "LAP-SAMS-BOOK4",
        "title": "Samsung Galaxy Book4 Intel Core 7 150U (16 GB RAM, 512 GB SSD, Full Metal)",
        "brand": "Samsung",
        "category": "Laptops",
        "sub_category": "Premium Ultrabook",
        "price": 79990.0,
        "original_price": 94990.0,
        "discount_pct": 15.8,
        "rating": 4.5,
        "rating_count": 4800,
        "stock": 30,
        "cost_price": 68000.0,
        "monthly_sales_units": 420,
        "image_url": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop&q=80",
        "description": "Seamless Galaxy Ecosystem continuity. Link to Windows, Phone as connected camera, Quick Share, and full aluminum unibody.",
        "specs": {"Processor": "Intel Core 7 150U (10 Cores, up to 5.4 GHz)", "RAM": "16 GB LPDDR5", "Storage": "512 GB NVMe SSD (Expandable)", "Display": "15.6 inch FHD Anti-Glare", "Weight": "1.55 kg", "Battery": "54 Wh (65W Type-C adapter)"},
        "features": ["Galaxy Ecosystem Integration", "All-metal Slim Chassis", "65W Compact USB-C Charger", "Dolby Atmos Speakers"]
    },

    # More Audio & Wearables
    {
        "id": "AUD-JBL-FLIP6",
        "title": "JBL Flip 6 Portable 30W Bluetooth Speaker (Midnight Black, IP67)",
        "brand": "JBL",
        "category": "Audio",
        "sub_category": "Bluetooth Speakers",
        "price": 9999.0,
        "original_price": 13999.0,
        "discount_pct": 28.5,
        "rating": 4.6,
        "rating_count": 42100,
        "stock": 95,
        "cost_price": 7500.0,
        "monthly_sales_units": 2100,
        "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=600&auto=format&fit=crop&q=80",
        "description": "2-way speaker system with racetrack-shaped woofer, separate tweeter and dual passive bass radiators. IP67 waterproof and dustproof, 12 hours playtime.",
        "specs": {"Power": "30W RMS (20W woofer + 10W tweeter)", "Battery": "Up to 12 hours playback", "Waterproof": "IP67 waterproof and dustproof", "Bluetooth": "v5.1 with PartyBoost"},
        "features": ["PartyBoost Link Multiple Speakers", "Dual Passive Bass Radiators", "IP67 Rugged Build", "JBL Portable App EQ Tuning"]
    },
    {
        "id": "AUD-REAL-BUDS5",
        "title": "realme Buds Air 5 Pro ANC Bluetooth Earbuds (Sunrise White, 50dB ANC)",
        "brand": "realme",
        "category": "Audio",
        "sub_category": "TWS Earbuds",
        "price": 4999.0,
        "original_price": 7999.0,
        "discount_pct": 37.5,
        "rating": 4.5,
        "rating_count": 22300,
        "stock": 110,
        "cost_price": 3600.0,
        "monthly_sales_units": 3100,
        "image_url": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=600&auto=format&fit=crop&q=80",
        "description": "Flagship 50dB Active Noise Cancellation with coaxial dual drivers (11mm bass + 6mm planar tweeter), LDAC Hi-Res audio, and 40h total battery.",
        "specs": {"Driver": "11mm Bass Driver + 6mm Micro-planar Tweeter", "ANC": "50dB Deep Sea Noise Cancellation 2.0", "Battery": "Up to 40 hours total playback", "Codec": "LDAC, AAC, SBC"},
        "features": ["Coaxial Dual Drivers", "50dB Smart Active Noise Cancellation", "Hi-Res Audio LDAC Certified", "40ms Low Latency Gaming"]
    },
    {
        "id": "WEAR-APPL-W9",
        "title": "Apple Watch Series 9 GPS 45mm (Midnight Aluminum Case with Sport Band)",
        "brand": "Apple",
        "category": "Wearables",
        "sub_category": "Smartwatch",
        "price": 41999.0,
        "original_price": 44900.0,
        "discount_pct": 6.5,
        "rating": 4.7,
        "rating_count": 7800,
        "stock": 25,
        "cost_price": 36000.0,
        "monthly_sales_units": 490,
        "image_url": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=600&auto=format&fit=crop&q=80",
        "description": "Powered by S9 SiP chip with Double Tap gesture, 2000 nits brighter Always-On display, on-device Siri, and Precision Finding for iPhone.",
        "specs": {"Processor": "Apple S9 SiP 64-bit dual-core", "Display": "Always-On Retina OLED up to 2000 nits", "Sensors": "ECG, Blood Oxygen, Temperature sensing, Heart Rate", "Water Resistance": "50 meters WR50"},
        "features": ["Magic Double Tap Gesture", "On-Device Siri with Health Data Access", "Crash Detection & Fall Detection", "Carbon Neutral Combinations"]
    },
    {
        "id": "WEAR-BO-LUNAR",
        "title": "boAt Lunar Vista 1.52-inch Round HD Display Smartwatch (Active Black)",
        "brand": "boAt",
        "category": "Wearables",
        "sub_category": "Smartwatch",
        "price": 1299.0,
        "original_price": 7990.0,
        "discount_pct": 83.7,
        "rating": 4.0,
        "rating_count": 86000,
        "stock": 310,
        "cost_price": 780.0,
        "monthly_sales_units": 11000,
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80",
        "description": "Classic circular metallic design, premium 1.52-inch round display with 550 nits brightness, Bluetooth calling, and 100+ sports modes.",
        "specs": {"Display": "1.52 inch HD Round Display 550 nits", "Calling": "Single-chip Bluetooth Calling", "Battery": "Up to 7 days standby (2 days calling)", "Durability": "IP68 water & dust proof"},
        "features": ["Classic Round Dial Metallic Frame", "Single-chip Bluetooth Calling", "100+ Sports Modes & Watch Faces", "Crest App Ecosystem"]
    },

    # More Appliances
    {
        "id": "HOME-SONY-BRAV55",
        "title": "Sony BRAVIA 2 55-inch 4K Ultra HD Smart LED Google TV (K-55S25B)",
        "brand": "Sony",
        "category": "Appliances",
        "sub_category": "Smart TVs",
        "price": 57990.0,
        "original_price": 99900.0,
        "discount_pct": 41.9,
        "rating": 4.6,
        "rating_count": 18200,
        "stock": 28,
        "cost_price": 47000.0,
        "monthly_sales_units": 610,
        "image_url": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=600&auto=format&fit=crop&q=80",
        "description": "Lifelike colors powered by 4K Processor X1 with Live Color technology. Dolby Audio, Open Baffle speakers, and PlayStation 5 auto HDR tone mapping.",
        "specs": {"Display": "55 inch 4K Ultra HD (3840x2160) Motionflow XR 100", "Processor": "4K Processor X1", "Audio": "20W Open Baffle with Dolby Audio", "OS": "Google TV with Apple AirPlay 2"},
        "features": ["4K Processor X1 Realism", "PS5 Exclusive Auto HDR & ALLM", "Google TV with Voice Search", "X-Protection PRO Shield"]
    },
    {
        "id": "HOME-DAIK-15AC",
        "title": "Daikin 1.5 Ton 5 Star Inverter Split AC (Copper, Triple Display, FTKM50U)",
        "brand": "Daikin",
        "category": "Appliances",
        "sub_category": "Air Conditioners",
        "price": 44990.0,
        "original_price": 67200.0,
        "discount_pct": 33.0,
        "rating": 4.5,
        "rating_count": 15400,
        "stock": 35,
        "cost_price": 36500.0,
        "monthly_sales_units": 850,
        "image_url": "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=600&auto=format&fit=crop&q=80",
        "description": "Patented Swing Compressor with Dew Clean technology. Coanda airflow distribution reaches up to 16 meters without draft hitting body directly.",
        "specs": {"Capacity": "1.5 Ton (Ideal for rooms up to 150 sq ft)", "Energy Rating": "5 Star BEE (ISEER 5.2)", "Condenser": "100% Copper with Anti-corrosion treatment", "Noise Level": "32 dB quiet operation"},
        "features": ["Dew Clean Auto Evaporator Cleaning", "Coanda 3D Airflow for Uniform Cooling", "Triple Display Panel (Temp, Error, Power)", "Cools up to 54°C Ambient"]
    },
    {
        "id": "HOME-IFB-MICRO",
        "title": "IFB 30 L Convection Microwave Oven (30BRC2, Black)",
        "brand": "IFB",
        "category": "Appliances",
        "sub_category": "Microwaves",
        "price": 14490.0,
        "original_price": 19490.0,
        "discount_pct": 25.6,
        "rating": 4.4,
        "rating_count": 19800,
        "stock": 40,
        "cost_price": 11500.0,
        "monthly_sales_units": 680,
        "image_url": "https://images.unsplash.com/photo-1584992236310-6edddc08acff?w=600&auto=format&fit=crop&q=80",
        "description": "30 Litre capacity suitable for large families. Features 101 auto cook menus, rotisserie for tandoori kebabs, baking, defrosting, and steam clean.",
        "specs": {"Capacity": "30 Litres", "Modes": "Baking, Grilling, Reheating, Defrosting, Roasting", "Cavity": "Stainless Steel with Deodorize & Steam Clean", "Power": "2200W Convection, 900W Microwave"},
        "features": ["Motorised Rotisserie for Tandoori", "101 Indian Auto Cook Menus", "Disinfect & Steam Clean Cavity", "Fermentation Mode for Batter"]
    },
    {
        "id": "HOME-DYSON-V8",
        "title": "Dyson V8 Cordless Vacuum Cleaner (Nickel/Yellow)",
        "brand": "Dyson",
        "category": "Appliances",
        "sub_category": "Vacuum Cleaners",
        "price": 29900.0,
        "original_price": 43900.0,
        "discount_pct": 31.8,
        "rating": 4.6,
        "rating_count": 9200,
        "stock": 25,
        "cost_price": 23500.0,
        "monthly_sales_units": 320,
        "image_url": "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=600&auto=format&fit=crop&q=80",
        "description": "Powerful fade-free cordless suction driven by Dyson digital motor V8. Whole machine filtration traps 99.99% of microscopic particles down to 0.3 microns.",
        "specs": {"Suction Power": "115 AW in Max mode", "Run Time": "Up to 40 minutes fade-free suction", "Bin Volume": "0.54 L no-touch dirt emptying", "Weight": "2.61 kg lightweight handheld convertibility"},
        "features": ["De-tangling Motorbar Cleaner Head", "Transforms to Handheld in One Click", "No-touch Hygienic Bin Emptying", "Acoustically Engineered Quiet Operation"]
    },

    # More Fashion
    {
        "id": "FASH-NIKE-PEG40",
        "title": "Nike Air Zoom Pegasus 40 Road Running Shoes (White/Obsidian)",
        "brand": "Nike",
        "category": "Fashion",
        "sub_category": "Footwear",
        "price": 7995.0,
        "original_price": 11895.0,
        "discount_pct": 32.7,
        "rating": 4.6,
        "rating_count": 18400,
        "stock": 55,
        "cost_price": 5200.0,
        "monthly_sales_units": 1100,
        "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80",
        "description": "Springy ride for every run. Dual Zoom Air units at forefoot and heel paired with Nike React lightweight resilient foam.",
        "specs": {"Cushioning": "Dual Zoom Air Units + React Foam", "Upper": "Single-layer engineered mesh", "Weight": "288g (Men's size 9)", "Usage": "Road running, marathon training, daily fitness"},
        "features": ["Dual Zoom Air Units for Pop", "Engineered Midfoot Band Support", "Waffle Outsole Traction", "Breathable Mesh Upper"]
    },
    {
        "id": "FASH-RAYB-WAYF",
        "title": "Ray-Ban Original Wayfarer Classic Polarized Sunglasses (Green Classic G-15)",
        "brand": "Ray-Ban",
        "category": "Fashion",
        "sub_category": "Eyewear",
        "price": 8990.0,
        "original_price": 10590.0,
        "discount_pct": 15.1,
        "rating": 4.7,
        "rating_count": 6400,
        "stock": 40,
        "cost_price": 5800.0,
        "monthly_sales_units": 390,
        "image_url": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=600&auto=format&fit=crop&q=80",
        "description": "The most recognizable style in the history of sunglasses since 1952. Polarized crystal lenses eliminate 99% of reflected glare with 100% UV400 protection.",
        "specs": {"Lens Technology": "Polarized Crystal Green G-15", "Frame Material": "Polished Black Acetate", "Eye Size": "50mm Standard", "UV Protection": "100% UV400 Protection"},
        "features": ["Polarized Anti-Glare Precision", "Classic G-15 Green Crystal Lens", "Iconic Rivet Hinges", "Handcrafted in Italy"]
    },
    {
        "id": "FASH-ZARA-JACK",
        "title": "Roadster Men Solid Faux Leather Biker Jacket (Coffee Brown)",
        "brand": "Roadster",
        "category": "Fashion",
        "sub_category": "Men's Clothing",
        "price": 1999.0,
        "original_price": 5499.0,
        "discount_pct": 63.6,
        "rating": 4.1,
        "rating_count": 48200,
        "stock": 140,
        "cost_price": 1100.0,
        "monthly_sales_units": 3200,
        "image_url": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600&auto=format&fit=crop&q=80",
        "description": "Rugged biker jacket crafted with supple faux leather, Mandarin collar with snap button, multiple zip pockets, and warm quilted inner lining.",
        "specs": {"Material": "100% Polyurethane Faux Leather", "Lining": "100% Polyester Quilted", "Collar": "Mandarin with press stud closure", "Pockets": "4 external zippered, 1 internal safe pocket"},
        "features": ["Quilted Thermal Lining for Winter", "Smooth Heavy-Duty Metal Zippers", "Slim Tailored Silhouette", "Windproof Outer Shell"]
    },
    {
        "id": "FASH-WOOD-BOOTS",
        "title": "Woodland Men Camel Brown Nubuck Leather Ankle Boots (GC 0572)",
        "brand": "Woodland",
        "category": "Fashion",
        "sub_category": "Footwear",
        "price": 3895.0,
        "original_price": 5295.0,
        "discount_pct": 26.4,
        "rating": 4.4,
        "rating_count": 39400,
        "stock": 75,
        "cost_price": 2500.0,
        "monthly_sales_units": 1500,
        "image_url": "https://images.unsplash.com/photo-1520639888713-7851133b1ed0?w=600&auto=format&fit=crop&q=80",
        "description": "Iconic outdoor adventure boot made from heavy-gauge nubuck leather. Deep lugged rubber outsole for extreme traction on rocks, mud, and trails.",
        "specs": {"Upper Material": "Genuine Heavy Nubuck Leather", "Sole": "Grooved Rough-Terrain Rubber", "Closure": "Lace-up with rust-proof brass eyelets", "Ankle Height": "Mid Ankle Padded Collar"},
        "features": ["Water-resistant Genuine Nubuck", "Deep Cleat Lug Grip", "Padded Collar for Ankle Protection", "Indestructible Dual Stitching"]
    }
]

# Generate more realistic reviews and competitors to enrich RAG and Analytics
def enrich_database(db_path: str = "backend/data/flipkart.db"):
    from backend.data.db import get_connection, seed_db
    import json

    conn = get_connection(db_path)
    cur = conn.cursor()

    for p in ADDITIONAL_PRODUCTS:
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

        # Add competitor prices
        amazon_price = round(p["price"] * random.uniform(0.97, 1.05), -1)
        cur.execute("""
            INSERT INTO competitor_prices (product_id, competitor_name, price, in_stock, delivery_days, url)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (p["id"], "Amazon", amazon_price, 1, random.randint(1, 3), "https://amazon.in"))

        croma_price = round(p["price"] * random.uniform(0.98, 1.08), -1)
        cur.execute("""
            INSERT INTO competitor_prices (product_id, competitor_name, price, in_stock, delivery_days, url)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (p["id"], "Croma", croma_price, 1, random.randint(2, 4), "https://croma.com"))

        # Add 3-5 realistic reviews per product
        reviews_templates = [
            ("Excellent product, surpassed expectations! Value for money.", 5.0, {"Value for Money": 1.0, "Build": 0.9, "Performance": 1.0}),
            ("Solid performance and premium finish. Flipkart fast delivery as usual.", 4.5, {"Delivery": 1.0, "Performance": 0.8, "Build": 0.9}),
            ("Good overall, but slightly expensive compared to alternatives.", 4.0, {"Value for Money": 0.3, "Build": 0.8, "Performance": 0.8}),
            ("Battery life is decent, day-to-day usability is smooth.", 4.0, {"Battery": 0.6, "Performance": 0.7})
        ]
        for idx, (rev_title, rev_rating, aspects) in enumerate(reviews_templates):
            cur.execute("""
                INSERT INTO reviews (product_id, author, rating, title, review_text, aspects_json, verified_purchase, helpful_count, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                p["id"], f"Customer {idx+1}", rev_rating, rev_title,
                f"{rev_title} Tried it extensively for 3 weeks and thoroughly satisfied with {p['title']}.",
                json.dumps(aspects), 1, random.randint(15, 250), "2025-01-20"
            ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    enrich_database()
    print("Database enriched successfully.")
