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
    html, body, [class*="css"]  {{
        background-color: {colors['background']};
        font-family: 'Poppins Light', sans-serif;
        color: {colors['forest_green']};
    }}
    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Fahkwang', sans-serif;
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
st.markdown("Choose a category to explore simple, sustainable swaps and visualize your impact with illustrated insights.✨")

# ---------- CATEGORIES + ICONS ----------
categories = {
    "Plastic Pollution": {
        "icon": "icons/plastic.png",
        "swaps": {
            "Use a reusable bottle": {
                "impact": "Prevents ~1,460 bottles from entering landfills in 4 years.",
                "sdgs": ["12 - Responsible Consumption", "13 - Climate Action", "14 - Life Below Water"],
                "visual": "icons/bottle_impact.png"
            },
            "Try beeswax wrap": {
                "impact": "Avoids ~500 sq. ft. of plastic wrap waste yearly.",
                "sdgs": ["12", "14"],
                "visual": "icons/beeswax_impact.png"
            }
        }
    },
    "Fast Fashion": {
        "icon": "icons/fashion.png",
        "swaps": {
            "Shop secondhand": {
                "impact": "Reduces water use & emissions — ~2,000 gallons saved per outfit.",
                "sdgs": ["12", "13"],
                "visual": "icons/secondhand_impact.png"
            },
            "Choose natural fibers": {
                "impact": "Helps clothes biodegrade vs. releasing microplastics.",
                "sdgs": ["12", "14"],
                "visual": "icons/fibers_impact.png"
            }
        }
    }
    # Add other categories and swaps here
}

if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# ---------- CATEGORY SELECTION ----------
st.markdown("## 🌿 Choose a Category")
cat_cols = st.columns(3)
for i, (cat_name, cat_data) in enumerate(categories.items()):
    with cat_cols[i % 3]:
        if st.button(cat_name):
            st.session_state.selected_category = cat_name

selected = st.session_state.selected_category

# ---------- SWAP DROPDOWN + IMPACT VISUAL ----------
if selected:
    st.image(categories[selected]["icon"], width=80)
    st.subheader(f"{selected}")
    swap_options = list(categories[selected]["swaps"].keys())
    chosen_swap = st.selectbox("Pick a sustainable swap:", swap_options, key=f"select_{selected}")

    if chosen_swap:
        swap_info = categories[selected]["swaps"][chosen_swap]
        st.image(swap_info["visual"], width=200)
        st.markdown(f"""
            <div class='impact-box'>
                <h4>🌍 Your Impact:</h4>
                <p>{swap_info['impact']}</p>
                <h5>✅ Supports these UN Goals:</h5>
{''.join([f"<span class='sdg-tag'>{sdg}</span>" for sdg in swap_info['sdgs']])}
            </div>
        """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("Created with 💚 by The Eco Connection")
