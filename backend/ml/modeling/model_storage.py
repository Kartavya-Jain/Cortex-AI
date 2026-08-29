import joblib
from pathlib import Path
MODEL_DIR = Path(__file__).resolve().parent.parent / "saved_models"
MODEL_DIR.mkdir(exist_ok=True)
def save_model(model, file_name="best_model.pkl"):
    model_path = MODEL_DIR / file_name
    joblib.dump(model, model_path)
    return {
        "status": "saved",
        "model_path": str(model_path)
    }
def load_model(filename="best_model.pkl"):
    model_path = MODEL_DIR / filename
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found: {model_path}"
        )
    return joblib.load(model_path)