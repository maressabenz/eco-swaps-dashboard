import streamlit as st
import matplotlib.pyplot as plt

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
st.markdown("Choose a category to explore simple, sustainable swaps and see your potential impact visualized with helpful charts.✨")

# ---------- SWAPS DATA ----------
categories = {
    "Plastic Pollution": {
        "swaps": {
            "Use a reusable bottle": {
                "impact": "Prevents ~1,460 bottles from entering landfills in 4 years.",
                "sdgs": ["12 - Responsible Consumption", "13 - Climate Action", "14 - Life Below Water"],
                "chart": [1460, 0]
            },
            "Try beeswax wrap": {
                "impact": "Avoids ~500 sq. ft. of plastic wrap waste yearly.",
                "sdgs": ["12", "14"],
                "chart": [500, 0]
            }
        }
    },
    "Fast Fashion": {
        "swaps": {
            "Shop secondhand": {
                "impact": "Reduces water use & emissions — ~2,000 gallons saved per outfit.",
                "sdgs": ["12", "13"],
                "chart": [2000, 0]
            },
            "Choose natural fibers": {
                "impact": "Helps clothes biodegrade vs. releasing microplastics.",
                "sdgs": ["12", "14"],
                "chart": [1, 0]
            }
        }
    }
}

if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# ---------- CATEGORY SELECTION ----------
st.markdown("## 🌿 Choose a Category")
selected_category = st.selectbox("Pick a category to explore:", list(categories.keys()))

if selected_category:
    st.subheader(f"{selected_category}")
    swap_options = list(categories[selected_category]["swaps"].keys())
    chosen_swap = st.selectbox("Pick a sustainable swap:", swap_options, key=f"select_{selected_category}")

    if chosen_swap:
        swap_info = categories[selected_category]["swaps"][chosen_swap]
        st.markdown(f"""
            <div class='impact-box'>
                <h4>🌍 Your Impact:</h4>
                <p>{swap_info['impact']}</p>
                <h5>✅ Supports these UN Goals:</h5>
                {''.join([f"<span class='sdg-tag'>{sdg}</span>" for sdg in swap_info['sdgs']])}
            </div>
        """, unsafe_allow_html=True)

        # Display chart
        st.markdown("### 📊 Estimated Impact Visualization")
        fig, ax = plt.subplots()
        ax.bar(["With this swap"], [swap_info["chart"][0]], color=colors["accent_orange"])
        ax.set_ylabel("Estimated Units Saved")
        st.pyplot(fig)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("Created with 💚 by The Eco Connection")
