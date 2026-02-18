import streamlit as st
import joblib
import numpy as np

st.markdown("""
            <style>        
            {background.color:blue;}
            </style>
            """, unsafe_allow_html=True)

# Load the trained model
model = joblib.load("model.pkl")

st.title("🐝 Honey Yield Prediction App")
st.write("This AI application predicts honey yield (kg) based on environmental and hive management factors.")
st.markdown("**PREPARED BY FUTURE PROGRAMMER GROUP**")

# --- User Inputs ---
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=10.0)
temperature = st.number_input("Average Temperature (°C)", min_value=0.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, step=0.1)
num_hives = st.number_input("Number of Hives", min_value=1, step=1)

hive_type = st.selectbox("Hive Type", ["traditional", "modern"])
colony_strength = st.selectbox("Colony Strength", ["weak", "medium", "strong"])
disease_status = st.selectbox("Disease Status", ["no", "yes"])
experience_years = st.number_input("Beekeeper Experience (years)", min_value=0, step=1)
inspection_frequency = st.number_input("Inspection Frequency (per month)", min_value=0, step=1)

# --- Encode categorical inputs ---
hive_type_modern = 1 if hive_type == "modern" else 0
colony_strength_medium = 1 if colony_strength == "medium" else 0
colony_strength_strong = 1 if colony_strength == "strong" else 0
disease_status_yes = 1 if disease_status == "yes" else 0

# --- Prepare input vector ---
input_data = np.array([[rainfall, temperature, humidity, num_hives,
                        experience_years, inspection_frequency,
                        hive_type_modern, colony_strength_medium,
                        colony_strength_strong, disease_status_yes]])

# --- Prediction ---
if st.button("Predict Honey Yield"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Honey Yield: {prediction[0]:.2f} kg")


# --- Footer --- 
st.markdown("---")
st.markdown("© 2026  Programmer Group all the best")
