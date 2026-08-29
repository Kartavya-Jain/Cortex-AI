from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
def get_models(problem_type):
    if problem_type == "regression":
        return {
            "linear_regression": LinearRegression(),
            "random_forest": RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )
        }
    elif problem_type == "classification":
        return {
            "logistic_regression": LogisticRegression(
                max_iter=1000
            ),
            "random_forest": RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )
        }
    else:
        raise ValueError(f"Unsupported problem type: {problem_type}")