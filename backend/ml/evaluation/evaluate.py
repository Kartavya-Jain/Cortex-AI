import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
def evaluate_model(model, X, y):
    """
    Evaluate a trained regression model.
    Returns:
            dict containing predictions and evaluation metrics.
    """
    predicted = model.predict(X)
    actual = np.asarray(y)
    predicted = np.asarray(predicted)
    absolute_error = np.abs(actual - predicted)
    error_percent = np.zeros_like(actual, dtype=float)
    non_zero = actual != 0
    #Avoid division by zero
    error_percent[non_zero] = (
        absolute_error[non_zero] / np.abs(actual[non_zero])
    ) * 100
    result = {
        "actual": actual,
        "predicted": predicted,
        "absolute_error": absolute_error,
        "error_percent": error_percent,
        "test_rows": len(actual),
        "average_actual_price": np.mean(actual),
        "average_predicted_price": np.mean(predicted),
        "mae": mean_absolute_error(actual, predicted),
        "mean_error_percent": np.mean(error_percent),
        "rmse": np.sqrt(
            mean_squared_error(actual, predicted)
        ),
        "r2_score": r2_score(actual, predicted),
        "min_absolute_error": np.min(absolute_error),
        "max_absolute_error": np.max(absolute_error)
    }
    return result