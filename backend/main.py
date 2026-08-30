from fastapi import FastAPI
from api.upload import router as upload_router
from api.predict import router as predict_router
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI(
    title="Cortex-AI",
    description="An AI-powered autoML and Data Analysis Platform",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
app.include_router(predict_router, prefix="/predict", tags=["Predict"])
@app.get("/")
def home():
    return{
        "message": "Welcome to Cortex-AI",
        "status": "Running"
    }