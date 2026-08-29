from fastapi import APIRouter
import joblib
import pandas as pd
from ml.modeling.predict import predict
router = APIRouter()
MODEL_PATH = "ml/saved_models/best_model.pkl"
model = joblib.load(MODEL_PATH)
@router.get("/")
def prediction_home():
    return {
        "message": "Prediction API working"
    }
@router.post("/")
def make_prediction(data: dict):
    X = pd.DataFrame([data])
    result = predict(model, X)
    return {
        "prediction": result[0]
    }