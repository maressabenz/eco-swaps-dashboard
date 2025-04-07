import streamlit as st

# ---------- CONFIG ----------
st.set_page_config(page_title="Eco-Friendly Swaps", layout="centered", page_icon="🌿")

# ---------- BRAND COLORS ----------
colors = {
    "background": "#ffe8d6",
    "accent_orange": "#d86123",
    "soft_sage": "#bab691",
    "deep_olive": "#4e5830",
    "forest_green": "#485d3a",
    "dusty_teal": "#6d9c94",
    "earthy_moss": "#7e8662"
}

# ---------- STYLING ----------
st.markdown(f"""
    <style>
    body {{
        background-color: {colors['background']};
        font-family: 'Georgia', serif;
        color: {colors['forest_green']};
    }}
    .impact-box {{
        background-color: {colors['soft_sage']};
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
    }}
    .sdg-tag {{
        background-color: {colors['dusty_teal']};
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.8em;
        margin-right: 5px;
    }}
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🌿 Eco-Friendly Swaps Dashboard")
st.markdown("Choose a category to explore simple, sustainable swaps and track your impact.✨")

# ---------- CATEGORIES + ICONS ----------
categories = {
    "Plastic Pollution": {
        "icon": "icons/plastic.png",
        "swaps": {
            "Use a reusable bottle": {
                "impact": "Prevents ~1,460 bottles from entering landfills in 4 years.",
                "sdgs": ["12 - Responsible Consumption", "13 - Climate Action", "14 - Life Below Water"]
            },
            "Try beeswax wrap": {
                "impact": "Avoids ~500 sq. ft. of plastic wrap waste yearly.",
                "sdgs": ["12", "14"]
            }
        }
    },
    "Fast Fashion": {
        "icon": "icons/fashion.png",
        "swaps": {
            "Shop secondhand": {
                "impact": "Reduces water use & emissions — ~2,000 gallons saved per outfit.",
                "sdgs": ["12", "13"]
            },
            "Choose natural fibers": {
                "impact": "Helps clothes biodegrade vs. releasing microplastics.",
                "sdgs": ["12", "14"]
            }
        }
    },
    "Reusable Alternatives": {
        "icon": "icons/reusables.png",
        "swaps": {
            "Bring a cloth tote bag": {
                "impact": "Saves ~1,000 plastic bags per person yearly.",
                "sdgs": ["12", "14"]
            },
            "Use cloth towels": {
                "impact": "Reduces ~3,000 paper towels/year and saves trees.",
                "sdgs": ["12", "15"]
            }
        }
    },
    "Eco-Friendly Products": {
        "icon": "icons/products.png",
        "swaps": {
            "Use shampoo bars": {
                "impact": "No plastic packaging, less water used.",
                "sdgs": ["12", "6 - Clean Water"]
            },
            "DIY vinegar cleaner": {
                "impact": "Avoids harsh chemicals in water systems.",
                "sdgs": ["6", "12"]
            }
        }
    },
    "Wildlife & Ecosystems": {
        "icon": "icons/wildlife.png",
        "swaps": {
            "Choose reef-safe sunscreen": {
                "impact": "Protects coral reefs from bleaching toxins.",
                "sdgs": ["14"]
            },
            "Avoid microbeads in products": {
                "impact": "Prevents synthetic particles harming marine life.",
                "sdgs": ["12", "14"]
            }
        }
    },
    "Container Gardening": {
        "icon": "icons/gardening.png",
        "swaps": {
            "Grow your own herbs": {
                "impact": "Reduces emissions & packaging from store-bought herbs.",
                "sdgs": ["11 - Sustainable Cities", "13"]
            },
            "Start composting": {
                "impact": "Diverts food waste & lowers methane emissions.",
                "sdgs": ["12", "13", "15"]
            }
        }
    }
}

if "selected_category" not in st.session_state:
    st.session_state.selected_category = None
if "selected_swaps" not in st.session_state:
    st.session_state.selected_swaps = []

# ---------- DISPLAY CATEGORY ICONS ----------
st.markdown("## 🌿 Choose a Category")
cat_cols = st.columns(3)
for i, (cat_name, cat_data) in enumerate(categories.items()):
    with cat_cols[i % 3]:
        if st.button(cat_name):
            st.session_state.selected_category = cat_name

selected = st.session_state.selected_category

# ---------- DISPLAY SWAPS ----------
if selected:
    st.image(categories[selected]["icon"], width=80)
    st.subheader(f"{selected}")
    for swap_text, swap_info in categories[selected]["swaps"].items():
        if st.button(swap_text, key=swap_text):
            if swap_text not in st.session_state.selected_swaps:
                st.session_state.selected_swaps.append(swap_text)
            st.markdown(f"""
                <div class='impact-box'>
                    <h4>🌍 Your Impact:</h4>
                    <p>{swap_info['impact']}</p>
                    <h5>✅ Supports these UN Goals:</h5>
                    {''.join([f"<span class='sdg-tag'>{sdg}</span>" for sdg in swap_info['sdgs']])}
                </div>
            """, unsafe_allow_html=True)

# ---------- TRACKER ----------
if st.session_state.selected_swaps:
    st.markdown("## 🌟 My Impact So Far")
    st.markdown("You're already making changes that matter. Here's what you've committed to:")
    for swap in st.session_state.selected_swaps:
        st.markdown(f"✅ {swap}")
    st.success(f"Total swaps: {len(st.session_state.selected_swaps)}")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("Created with 💚 by The Eco Connection")
