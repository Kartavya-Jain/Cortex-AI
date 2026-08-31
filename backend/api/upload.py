from fastapi import APIRouter, UploadFile, File
from fastapi.encoders import jsonable_encoder
from ml.analysis.analysis import analyze_dataset
from ml.preprocessing.preprocess import preprocess_dataset
from ml.modeling.pipeline import run_ml_pipeline
import shutil
from pathlib import Path
import pandas as pd
import io
import numpy as np
import json
def make_json_safe(obj):
    if isinstance(obj, dict):
        return {str(k): make_json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [make_json_safe(v) for v in obj]
    if isinstance(obj, np.generic):
        return obj.item()
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    return str(obj)
BASE_DIR =Path(__file__).resolve().parent.parent
UPLOAD_FOLDER=BASE_DIR/"uploads"
UPLOAD_FOLDER.mkdir(exist_ok=True)
router=APIRouter()
@router.get("/")
def upload_home():
    return{
        "message": "Upload API working"
    }
@router.post("/csv")
async def upload_csv(file: UploadFile = File(...)):
    file_path=UPLOAD_FOLDER/file.filename
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    with open(file_path, "rb") as f:
        content=f.read()
    content = content.replace(b"\x00", b"")
    df = pd.read_csv(io.BytesIO(content), encoding="latin1", engine="python", on_bad_lines="skip")
    dataset_info=analyze_dataset(df)
    ml_result = run_ml_pipeline(df)
    final_evaluation = ml_result["final_evaluation"]
    print("Original shape:", df.shape)
    ml_result["preprocessing"]["artifacts"].pop("scaler", None)
    dataset_info = make_json_safe(dataset_info)
    ml_result = make_json_safe(ml_result)
    final_evaluation = ml_result.get("final_evaluation")
    if final_evaluation:
        ml_result["final_evaluation"] = {
            key: value
            for key, value in final_evaluation.items()
            if key not in ["actual", "predicted", "absolute_error", "error_percent"]
        }
    return {
        "filename": file.filename,
        "dataset": dataset_info,
        "ml": ml_result,
        "evaluation": final_evaluation
    }