import streamlit as st
import joblib
import numpy as np
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px

# Load model and columns
model = joblib.load('bangalore_home_price_model.pkl')
columns = joblib.load('model_columns.pkl')

# Extract location names from columns
location_names = [col for col in columns if col not in ['total_sqft', 'bath', 'bhk']]

# Sample coordinates for some locations (you can add more as needed)
location_coords = {
    'Whitefield': [12.9698, 77.7499],
    'Electronic City': [12.8380, 77.6770],
    'Marathahalli': [12.9560, 77.7019],
    'HSR Layout': [12.9116, 77.6412],
    'Indira Nagar': [12.9719, 77.6412],
}

# App Title
st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")
st.title("🏠 Bangalore House Price Predictor")

# Input Fields
location = st.selectbox("📍 Select Location", sorted(location_names))
sqft = st.slider("📐 Total Square Feet", 500, 5000, 1000, step=50)
bath = st.slider("🚿 Number of Bathrooms", 1, 5, 2)
bhk = st.slider("🛏️ Number of Bedrooms (BHK)", 1, 5, 2)

# Prediction
if st.button("Predict Price"):
    try:
        loc_index = np.where(columns == location)[0][0]
        x = np.zeros(len(columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        x[loc_index] = 1

        price = model.predict([x])[0]

        st.success(f"💰 Predicted Price: ₹{round(price, 2)} lakhs")

        # 📊 Show input summary chart
        df_input = pd.DataFrame({
            "Feature": ["Square Feet", "Bathrooms", "BHK", "Price (Lakh)"],
            "Value": [sqft, bath, bhk, round(price, 2)]
        })
        fig = px.bar(df_input, x="Feature", y="Value", color="Feature", title="📈 Input Summary")
        st.plotly_chart(fig, use_container_width=True)

        # 🗺️ Show map if coordinates available
        if location in location_coords:
            lat, lon = location_coords[location]
            st.subheader("📍 Approximate Property Location")
            m = folium.Map(location=[lat, lon], zoom_start=13)
            folium.Marker([lat, lon], popup=location).add_to(m)
            st_folium(m, width=700)

        else:
            st.info("🌍 Map view not available for this location.")

    except Exception as e:
        st.error(f"❌ Error: {e}")
