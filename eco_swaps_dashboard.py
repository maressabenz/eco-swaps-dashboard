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
        text-decoration: none;
    }}
    a {{
        text-decoration: none;
    }}
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🌿 Eco-Friendly Swaps Dashboard")
st.markdown("Choose a category to explore simple, sustainable swaps and see your impact visualized through friendly reminders and stats.✨")

# ---------- SWAPS DATA ----------
categories = {
    "Plastic Pollution": {
        "swaps": {
            "Use a reusable bottle": {
                "impact": "Prevents ~1,460 plastic bottles from entering landfills in 4 years.",
                "infographic": "That’s the same as avoiding 30 pounds of plastic waste 💧",
                "sdgs": ["12 - Responsible Consumption", "13 - Climate Action", "14 - Life Below Water"]
            },
            "Try beeswax wrap": {
                "impact": "Avoids ~500 sq. ft. of plastic wrap waste yearly.",
                "infographic": "That’s enough wrap to cover your entire kitchen table every week 🍯",
                "sdgs": ["12 - Responsible Consumption", "14 - Life Below Water"]
            }
        }
    },
    "Fast Fashion": {
        "swaps": {
            "Shop secondhand": {
                "impact": "Reduces water use — ~2,000 gallons saved per outfit.",
                "infographic": "That’s the same as 30 showers 🚿",
                "sdgs": ["12 - Responsible Consumption", "13 - Climate Action"]
            },
            "Choose natural fibers": {
                "impact": "Helps clothes biodegrade vs. releasing microplastics.",
                "infographic": "Less synthetic fiber = less microplastic in the ocean 🌊",
                "sdgs": ["12 - Responsible Consumption", "14 - Life Below Water"]
            }
        }
    },
    "Reusable Alternatives": {
        "swaps": {
            "Bring a cloth tote bag": {
                "impact": "Saves ~1,000 plastic bags per person yearly.",
                "infographic": "That’s like skipping 20 full trash bags worth of plastic 🛍️",
                "sdgs": ["12 - Responsible Consumption", "14 - Life Below Water"]
            },
            "Use cloth towels": {
                "impact": "Reduces ~3,000 paper towels/year and saves trees.",
                "infographic": "Enough to save one small tree 🌳",
                "sdgs": ["12 - Responsible Consumption", "15 - Life on Land"]
            }
        }
    },
    "Eco-Friendly Products": {
        "swaps": {
            "Use shampoo bars": {
                "impact": "No plastic packaging and less water used.",
                "infographic": "One bar = 3 bottles saved from the landfill 🧼",
                "sdgs": ["12 - Responsible Consumption", "6 - Clean Water"]
            },
            "DIY vinegar cleaner": {
                "impact": "Avoids harsh chemicals in water systems.",
                "infographic": "Just vinegar + citrus peels = sparkling and safe 🍋",
                "sdgs": ["6 - Clean Water", "12 - Responsible Consumption"]
            }
        }
    },
    "Wildlife & Ecosystems": {
        "swaps": {
            "Choose reef-safe sunscreen": {
                "impact": "Protects coral reefs from bleaching toxins.",
                "infographic": "Sunscreen without oxybenzone = happier fish 🐠",
                "sdgs": ["14 - Life Below Water"]
            },
            "Avoid microbeads in products": {
                "impact": "Prevents plastic particles harming marine life.",
                "infographic": "One tube of scrub can contain 300,000 microbeads 🐚",
                "sdgs": ["12 - Responsible Consumption", "14 - Life Below Water"]
            }
        }
    },
    "Container Gardening": {
        "swaps": {
            "Grow your own herbs": {
                "impact": "Reduces packaging and emissions from store-bought herbs.",
                "infographic": "Fresh herbs on hand = no plastic clamshells 🌿",
                "sdgs": ["11 - Sustainable Cities", "13 - Climate Action"]
            },
            "Start composting": {
                "impact": "Diverts food waste & lowers methane emissions.",
                "infographic": "Every 10 lbs composted = 2.5 lbs less methane ☁️",
                "sdgs": ["12 - Responsible Consumption", "13 - Climate Action", "15 - Life on Land"]
            }
        }
    }
}

# ---------- CATEGORY SELECTION ----------
selected_category = st.selectbox("💡 Pick a category to explore:", list(categories.keys()))

# ---------- SWAP SELECTION ----------
if selected_category:
    st.subheader(f"{selected_category}")
    swap_options = list(categories[selected_category]["swaps"].keys())
    chosen_swap = st.selectbox("🌱 Pick a sustainable swap:", swap_options, key=f"select_{selected_category}")

    if chosen_swap:
        swap_info = categories[selected_category]["swaps"][chosen_swap]
        st.markdown(f"""
            <div class='impact-box'>
                <h4>🌍 Your Impact:</h4>
                <p>{swap_info['impact']}</p>
                <h5>📊 Understanding Your Impact:</h5>
                <p><em>{swap_info['infographic']}</em></p>
                <h5>✅ Supports these UN Goals:</h5>
                {''.join([
                    f"<a href='https://sdgs.un.org/goals/goal{sdg.split(' ')[0]}' target='_blank'><span class='sdg-tag'>{sdg}</span></a>"
                    for sdg in swap_info['sdgs']
                ])}
            </div>
        """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("Created with 💚 by Maressa Benz - The Eco Connection")
