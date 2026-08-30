from fastapi import APIRouter
import joblib
import pandas as pd
from pathlib import Path
from ml.modeling.predict import predict
router = APIRouter()
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "ml/saved_models/best_model.pkl"
FEATURE_PATH = BASE_DIR / "ml/saved_models/feature_columns.pkl"
ARTIFACT_PATH = BASE_DIR / "ml"/"saved_models"/"preprocessing_artifacts.pkl"
model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURE_PATH)
artifacts = joblib.load(ARTIFACT_PATH)
@router.get("/")
def prediction_home():
    return {
        "message": "Prediction API working"
    }
@router.post("/")
def make_prediction(data: dict):
    X = pd.DataFrame([data])
    frequency_maps = artifacts["frequency_maps"]
    for column, mapping in frequency_maps.items():
        X[column] = X[column].map(mapping).fillna(0)
    X =pd.get_dummies(
        X,
        colums=artifacts["encoded_columns"],
        drop_first=True
        )
    X.reindex(columns=feature_columns, fill_value=0)
    result = predict(model, X)
    return {
        "prediction": result[0]
    }