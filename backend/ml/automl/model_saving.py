import joblib
from pathlib import Path
MODEL_FOLDER=Path(__file__).resolve().parent.parent / "saved_models"
MODEL_FOLDER.mkdir(exist_ok=True)
def save_model(model, model_name):
    file_path = MODEL_FOLDER / f"{model_name}.joblib"
    joblib.dump(model, file_path)
    report = {
        "model_name": model_name,
        "saved_path": str(file_path),
        "status": "Saved Successfully"
    }
    return file_path, report