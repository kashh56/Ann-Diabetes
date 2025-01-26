import pickle
import numpy as np

# Function to load the model and scaler
def load_model_and_predict(input_data):
    # Load model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Load scaler
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    # Scale the input data (assuming the input is a 1D array of features)
    input_data_scaled = scaler.transform([input_data])

    # Predict using the model
    prediction = model.predict(input_data_scaled)
    prediction_per = prediction * 100 
    # Convert the prediction to a binary outcome (0 or 1)
    if prediction >= 0.5:
        return f"Has Diabetes : The person has {prediction_per} % Chance of being diabetic"
    else:
        return f"Does Not Have Diabetes : The person has {prediction_per} % Chance of being diabetic"
