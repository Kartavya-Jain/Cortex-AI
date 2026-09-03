from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score
import numpy as np
from ml.evaluation.evaluate import evaluate_model
def evaluate_models(trained_models, X_test, y_test, problem_type):
    results = {}
    for name, model in trained_models.items():
        predictions = model.predict(X_test)
        if problem_type == "regression":
            evaluation = evaluate_model(model, X_test, y_test)
            results[name] = {
                "MAE": float(evaluation["mae"]),
                "RMSE": float(evaluation["rmse"]),
                "R2": float(evaluation["r2_score"])
            }
        elif problem_type == "classification":
            accuracy = accuracy_score(y_test, predictions)
            precision = precision_score(
                y_test,
                predictions,
                average="weighted",
                zero_division=0
            )
            recall = recall_score(
                y_test,
                predictions,
                average="weighted",
                zero_division=0
            )
            f1 = f1_score(
                y_test,
                predictions,
                average="weighted",
                zero_division=0
            )
            results[name] = {
                "accuracy": float(accuracy),
                "precision": float(precision),
                "recall": float(recall),
                "f1": float(f1)
            }
        else:
            raise ValueError(
                f"Unsupported problem type: {problem_type}"
            )
    return results