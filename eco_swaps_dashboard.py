import streamlit as st

# ---------- BRAND COLORS ----------
background_color = "#ffe8d6"
accent_orange = "#d86123"
soft_sage = "#bab691"
deep_olive = "#4e5830"
forest_green = "#485d3a"
dusty_teal = "#6d9c94"
earthy_moss = "#7e8662"

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Eco-Friendly Swaps Dashboard", layout="centered", page_icon="🌿")

# ---------- CUSTOM STYLING ----------
st.markdown(f"""
    <style>
        .reportview-container {{
            background-color: {background_color};
            color: {forest_green};
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {forest_green};
            font-family: 'Georgia', serif;
        }}
        .impact-box {{
            background-color: {soft_sage};
            border-radius: 10px;
            padding: 1em;
            margin-top: 1em;
        }}
        .sdg-tag {{
            background-color: {dusty_teal};
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.8em;
            margin-right: 5px;
        }}
        .sdg-card {{
            background-color: {soft_sage};
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }}
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
# 🌱 Thoughtful Living Dashboard
### Small swaps, big ripples.
Select a swap to learn its impact and the global goals you're supporting.✨
""")

# ---------- SDG EDUCATION SECTION ----------
st.markdown("## 🌍 Meet the SDGs")
sdg_data = [
    ("♻️ Goal 12: Responsible Consumption & Production", 
     "When we consume less and choose better, we reduce waste, pollution, and pressure on the planet’s resources. Every thoughtful swap supports a more balanced world."),
    
    ("🌎 Goal 13: Climate Action", 
     "Small actions like composting or cutting plastic help lower emissions and slow climate change. It’s not about doing it all — it’s about doing what you can."),
    
    ("🌊 Goal 14: Life Below Water", 
     "Plastic-free swaps and reef-safe products protect ocean life — from coral reefs to sea turtles. What you skip on land helps life in the sea."),
    
    ("🌱 Goal 15: Life on Land", 
     "Organic gardening and reducing toxins help restore soil, support pollinators, and protect wildlife. Nature thrives when we make space for it."),
    
    ("💧 Goal 6: Clean Water & Sanitation", 
     "Swapping to natural cleaners and shampoos keeps harsh chemicals out of our water systems. Cleaner choices = cleaner streams, lakes, and oceans."),
    
    ("🏙️ Goal 11: Sustainable Cities & Communities", 
     "Growing herbs on a windowsill or balcony adds greenery to our cities and reduces packaging waste. Yes, even your little container garden counts.")
]

for title, desc in sdg_data:
    st.markdown(f"""
        <div class="sdg-card">
            <h5>{title}</h5>
            <p>{desc}</p>
        </div>
    """, unsafe_allow_html=True)

# ---------- SWAPS DATA ----------
category_icons = {
    "Plastic Pollution": "🧴",
    "Fast Fashion": "🛍️",
    "Reusable Alternatives": "♻️",
    "Eco-Friendly Products": "🧼",
    "Wildlife & Ecosystems": "🐢",
    "Container Gardening": "🌿"
}

swaps = {
    "Plastic Pollution": {
        "Swap plastic bottles for reusable": {
            "impact": "Prevents ~1,460 bottles from entering landfills in 4 years.",
            "sdgs": ["12 - Responsible Consumption", "13 - Climate Action", "14 - Life Below Water"]
        },
        "Switch to beeswax wrap": {
            "impact": "Avoids ~500 sq. ft. of plastic wrap waste yearly.",
            "sdgs": ["12", "14"]
        }
    },
    "Fast Fashion": {
        "Shop secondhand": {
            "impact": "Reduces water use & emissions — ~2,000 gallons saved per outfit.",
            "sdgs": ["12", "13"]
        },
        "Choose natural fibers": {
            "impact": "Helps biodegrade clothing vs. releasing microplastics.",
            "sdgs": ["12", "14"]
        }
    },
    "Reusable Alternatives": {
        "Use cloth shopping bags": {
            "impact": "Saves ~1,000 plastic bags per person yearly.",
            "sdgs": ["12", "14"]
        },
        "Swap paper towels for cloth": {
            "impact": "Reduces ~3,000 towels/year and saves trees.",
            "sdgs": ["12", "15"]
        }
    },
    "Eco-Friendly Products": {
        "Use natural shampoo bars": {
            "impact": "No plastic packaging, less water used in production.",
            "sdgs": ["12", "6 - Clean Water"]
        },
        "DIY vinegar cleaner": {
            "impact": "Avoids harsh chemicals in water systems.",
            "sdgs": ["6", "12"]
        }
    },
    "Wildlife & Ecosystems": {
        "Choose reef-safe sunscreen": {
            "impact": "Protects coral reefs from bleaching toxins.",
            "sdgs": ["14"]
        },
        "Avoid microplastic-based products": {
            "impact": "Prevents synthetic particles harming aquatic life.",
            "sdgs": ["12", "14"]
        }
    },
    "Container Gardening": {
        "Grow herbs at home": {
            "impact": "Reduces emissions & packaging from store-bought herbs.",
            "sdgs": ["11 - Sustainable Cities", "13"]
        },
        "Start a compost bin": {
            "impact": "Diverts food waste & lowers methane emissions.",
            "sdgs": ["12", "13", "15"]
        }
    }
}

# ---------- USER INPUT USING BUTTONS ----------
st.markdown("## 🌿 Choose a Category")
selected_category = None
cols = st.columns(3)
categories = list(swaps.keys())

for i, category in enumerate(categories):
    with cols[i % 3]:
        if st.button(f"{category_icons[category]} {category}"):
            selected_category = category

if selected_category:
    st.markdown(f"## {category_icons[selected_category]} {selected_category}")
    
    swap = st.selectbox(
        "Now pick an eco-friendly swap:",
        list(swaps[selected_category].keys()),
        key=f"swap_select_{selected_category}"
    )

    if swap:
        info = swaps[selected_category][swap]
        st.markdown(f"""
            <div class="impact-box">
                <h4>🌍 Your Impact:</h4>
                <p>{info['impact']}</p>
                <h5>✅ Supports these UN Goals:</h5>
                {''.join([f'<span class="sdg-tag">{sdg}</span>' for sdg in info['sdgs']])}
            </div>
        """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("Created with 💚 by The Eco Connection")
