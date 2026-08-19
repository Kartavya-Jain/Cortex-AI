from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
import numpy as np
def evaluate_model(model, X_test, y_test, problem_type):
    y_pred=model.predict(X_test)
    if problem_type=="regression":
        report = {
            "problem_type": problem_type,
            "r2_score":round(r2_score(y_test,y_pred),4),
            "mae": round(mean_absolute_error(y_test,y_pred),4),
            "rmse": round(np.sqrt(mean_squared_error(y_test,y_pred)),4) 
        }
    else:
        report = {
            "problem_type": problem_type,
            "accuracy":round(accuracy_score(y_test,y_pred),4),
            "precision": round(precision_score(y_test,y_pred,average="weighted", zero_division=0),4),
            "recall": round(recall_score(y_test,y_pred,average="weighted",zero_division=0),4),
            "f1_score": round(f1_score(y_test,y_pred,average="weighted",zero_division=0),4)
        }
    return report