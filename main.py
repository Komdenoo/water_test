from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import water  # ✅ ensure class name is capitalized to match convention

# Initialize the FastAPI app
app = FastAPI(
    title="Water Potability Prediction",
    description="An API for predicting water potability"
)

# Load the trained model
with open(r"D:\Ml_pipeline dd\model.pkl", "rb") as f:
    model = pickle.load(f)

# Root endpoint
@app.get("/")
def index():
    return {"message": "Welcome to the Water Potability Prediction FastAPI!"}

# Prediction endpoint
@app.post("/predict")
def model_predict(water: water):
    # Create a DataFrame from the input data
    sample = pd.DataFrame({
        "ph": [water.ph],
        "Hardness": [water.Hardness],
        "Solids": [water.Solids],
        "Chloramines": [water.Chloramines],
        "Sulfate": [water.Sulfate],
        "Conductivity": [water.Conductivity],
        "Organic_carbon": [water.Organic_carbon],
        "Trihalomethanes": [water.Trihalomethanes],
        "Turbidity": [water.Turbidity]
    })

    # Make prediction
    predicted_value = model.predict(sample)[0]

    # Return response
    if predicted_value == 1:
        return {"prediction": "Water is consumable"}
    else:
        return {"prediction": "Water is not consumable"}