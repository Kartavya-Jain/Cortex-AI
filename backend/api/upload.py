from fastapi import APIRouter, UploadFile, File
from ml.analysis.analysis import analyze_dataset
from ml.preprocessing.preprocess import preprocess_dataset
import shutil
from pathlib import Path
import pandas as pd
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
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    df=pd.read_csv(file_path)
    dataset_info=analyze_dataset(df)
    cleaned_df, preprocessing_info=preprocess_dataset(df)
    return {
        "filename": file.filename,
        "dataset": dataset_info,
        "preprocessing": preprocessing_info
    }