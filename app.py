import streamlit as st
import json
from datetime import datetime

# ✅ Apply theme settings dynamically (like config.toml)
st.set_page_config(
    page_title="🌾 Schemes & Subsidy Auto-Match",
    page_icon="🌱",
    layout="centered",
)

# ✅ Custom CSS to match [theme] config
st.markdown(
    """
    <style>
    /* Global background and text */
    body, .stApp {
        background-color: #f2efdeff;
        color: #3a2f1e;
        font-family: 'sans-serif';
    }

    /* Make markdown and JSON text follow theme */
    .stMarkdown, .stJson {
        color: #3a2f1e !important;
    }

    /* Style selectbox (dropdown) */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important; /* secondaryBackgroundColor */
        color: #3a2f1e !important;
        border: 1px solid #d3d3d3;
        border-radius: 8px;
    }

    /* Style dropdown menu */
    div[data-baseweb="popover"] {
        background-color: #ffffff !important;
        color: #3a2f1e !important;
    }

    /* Style buttons to use primaryColor */
    button[kind="primary"] {
        background-color: #6b4e16 !important;
        color: white !important;
        border-radius: 8px;
    }

    /* Success + Warning boxes to match theme */
    .stSuccess {
        background-color: #e8e3d9 !important;
        border-left: 5px solid #6b4e16 !important;
        color: #3a2f1e !important;
    }
    .stWarning {
        background-color: #fff8e1 !important;
        border-left: 5px solid #ffb300 !important;
        color: #3a2f1e !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load farmers and schemes
with open("farmers.json", "r") as f:
    farmers = json.load(f)

with open("schemes.json", "r") as f:
    schemes = json.load(f)

# Function to match schemes
def match_schemes(farmer):
    matches = []
    for scheme in schemes:
        if (
            farmer["crop"] in scheme["eligibleCrops"]
            and farmer["landSize"] >= scheme["minLandSize"]
            and farmer["location"] == scheme["location"]
        ):
            deadline = datetime.strptime(scheme["deadline"], "%Y-%m-%d").strftime("%d %b %Y")
            matches.append(f"{scheme['name']} (Deadline: {deadline})")
    return matches

# Streamlit UI
st.title("🌾 Schemes & Subsidy Auto-Match")
st.write("Find government schemes automatically based on farmer profile.")

# Select farmer
farmer_names = {f["name"]: f for f in farmers}
selected_name = st.selectbox("Select Farmer", list(farmer_names.keys()))
farmer = farmer_names[selected_name]

st.subheader("👩‍🌾 Farmer Profile")
st.json(farmer)

# Show matching schemes
st.subheader("✅ Eligible Schemes")
matches



