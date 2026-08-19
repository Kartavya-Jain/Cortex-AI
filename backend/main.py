from fastapi import FastAPI
from api.upload import router as upload_router
app=FastAPI(
    title="Cortex-AI",
    description="An AI-powered autoML and Data Analysis Platform",
    version="1.0.0"
)
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
@app.get("/")
def home():
    return{
        "message": "Welcome to Cortex-AI",
        "status": "Running"
    }