import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
from function_to_load_model_and_predict_diabetes import load_model_and_predict



# Streamlit UI elements to collect input
st.title("Diabetes Prediction Model")

# Define the input fields for the user to fill in (7 features + SkinThickness)
age = st.number_input("Age", min_value=18, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=100.0, value=22.0)
BloodPressure = st.number_input("Blood Pressure", min_value=50, max_value=200, value=80)
glucose = st.number_input("Glucose Level", min_value=50, max_value=300, value=100)
insulin = st.number_input("Insulin Level", min_value=0, max_value=500, value=50)
pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.0, value=0.5)
pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)  # Add SkinThickness

# Create a button to submit the input and get the prediction
if st.button("Predict"):
    # Prepare the input data (including SkinThickness)
    input_data = [pregnancies, glucose, BloodPressure, skin_thickness, insulin, bmi, pedigree_function, age]

    # Call the function to load model and make a prediction
    prediction = load_model_and_predict(input_data)

    # Display the result
    st.write(f"The model predicts: {prediction}")

