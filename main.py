import joblib
import pandas as pd
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel , Field

app = FastAPI()
model = joblib.load("house_model.joblib")
features = joblib.load("house_features.joblib")

class HouseFeatures(BaseModel):
    MedInc: float = Field(gt =0, description="Median income in block group")
    HouseAge: float = Field(gt=0, description="Median house age in block group")
    AveRooms: float = Field(gt=0, description="Average number of rooms per household")
    AveBedrms: float = Field(gt=0, description="Average number of bedrooms per household")
    Population: float = Field(gt=0, description="Population in block group")
    AveOccup: float = Field(gt=0, description="Average number of household members")
    Latitude: float = Field(ge=32,le=42, description="Latitude of block group")
    Longitude: float = Field(ge=-125,le=-114, description="Longitude of block group")

@app.get("/")
def home():
    return{
        "message":"Welcome to the House Price Prediction Brother",
        "status":"running"
        
    }  

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    try:
        input_data = pd.DataFrame([features.dict()])
        prediction = model.predict(input_data)

        return {"predicted_price": prediction[0] * 10000}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))