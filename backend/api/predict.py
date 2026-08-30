from fastapi import APIRouter
import joblib
import pandas as pd
from pathlib import Path
from ml.modeling.predict import predict
router = APIRouter()
MODEL_PATH = "ml/saved_models/best_model.pkl"
BASE_DIR = Path(__file__).resolve().parent.parent
FEATURE_PATH = BASE_DIR / "ml/saved_models/feature_columns.pkl"
model = joblib.load(MODEL_PATH)
@router.get("/")
def prediction_home():
    return {
        "message": "Prediction API working"
    }
@router.post("/")
def make_prediction(data: dict):
    X = pd.DataFrame([data])
    feature_columns = joblib.load(FEATURE_PATH)
    X =X.reindex(columns=feature_columns, fill_value=0)
    result = predict(model, X)
    return {
        "prediction": result[0]
    }