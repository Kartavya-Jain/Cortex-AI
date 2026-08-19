import joblib
import pandas as pd
def predict(model_path, input_data):
    model=joblib.load(model_path)
    if isinstance(input_data,dict):
        input_data=pd.DataFrame([input_data])
    prediction=model.predict(input_data)
    report = {
        "prediction": prediction.tolist(),
        "status": "Prediction Successful"
    }
    return report