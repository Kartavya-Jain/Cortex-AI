from fastapi import APIRouter, UploadFile, File
from fastapi.encoders import jsonable_encoder
from ml.analysis.analysis import analyze_dataset
from ml.preprocessing.preprocess import preprocess_dataset
import shutil
from pathlib import Path
import pandas as pd
import io
import numpy as np
import json
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
    with open(file_path, "rb") as f:
        content=f.read()
    content = content.replace(b"\x00", b"")
    df = pd.read_csv(io.BytesIO(content), encoding="latin1", engine="python", on_bad_lines="skip")
    dataset_info=analyze_dataset(df)
    cleaned_df, preprocessing_info=preprocess_dataset(df)
    return jsonable_encoder ({
        "filename": file.filename,
        "dataset": dataset_info,
        "preprocessing": preprocessing_info
    })