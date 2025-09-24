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
    /* Global Background and Text */
    body, .stApp {
        background-color: #f2efdeff;
        color: #3a2f1e;
        font-family: 'sans-serif';
    }

    /* Ensure markdown and JSON text use the theme color */
    .stMarkdown {
        color: #3a2f1e;
    }

    /* Make dropdown (selectbox) white with black text */
    div[data-baseweb="select"] > div {
        background-color:  #ffffff !important;
        color: #000000 !important;  /* selected text color */
        border: 1px solid #d3d3d3;
        border-radius: 8px;
    }

    /* Dropdown menu background and text color */
    div[data-baseweb="popover"] {
        background-color:  #ffffff !important;
        color: #000000 !important;
    }

    /* Style farmer profile (st.json) container */
    .stJson {
        background-color:  #ffffff !important;
        color: #000000 !important;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.1);
    }

    /* Make selectbox label text black */
    label[data-baseweb="label"] {
        color: #000000 !important;
        font-weight: bold;
    }

    /* Make selected dropdown text black */
    div[data-baseweb="select"] span {
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








