import streamlit as st
import json
from datetime import datetime

# ✅ Set custom theme directly from app.py
st.set_page_config(
    page_title="🌾 Schemes & Subsidy Auto-Match",
    page_icon="🌱",
    layout="centered",  # or "wide"
)

st.markdown(
    """
    <style>
    /* Set global text color to black */
    body {
        background-color: #f2efdeff;
        color: #000000;
        font-family: 'sans-serif';
    }

    /* Make sure the main app container also uses the same background */
    .stApp {
        background-color: #f2efdeff;
    }

    /* Ensure markdown text & JSON text appear in black */
    .stMarkdown, .stJson {
        color: #000000 !important;
    }

    /* Style the dropdown (selectbox) */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important; /* white background */
        color: #000000 !important; /* black text */
        border-radius: 8px; /* rounded edges for a modern look */
        border: 1px solid #ccc; /* light border */
    }

    /* Style dropdown menu options */
    div[data-baseweb="popover"] {
        background-color: #ffffff !important; /* white dropdown menu */
        color: #000000 !important;
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
matches = match_schemes(farmer)

if matches:
    for m in matches:
        st.success(m)
else:
    st.warning("No matching schemes found.")

