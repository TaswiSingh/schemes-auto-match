import streamlit as st
import json
from datetime import datetime

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

