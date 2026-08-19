from ml.automl.problem_type import detect_problem_type
def recommend_model(df):
    problem_report=detect_problem_type(df)
    problem_type=problem_report["problem_type"]
    if problem_type=="regression":
        models=[
            "Linear Regression",
            "Random Forest Regressor",
            "Decision Tree Regressor",
            "Gradient Boosting Regressor",
            "XGBoost Regressor"
        ]
    elif problem_type=="classification":
        models=[
            "Logistic Regression",
            "Random Forest Classifier",
            "Decision Tree Classifier",
            "Gradient Boosting Classifier",
            "XGBoost Classifier"
        ]
    else:
        models=[]
    recommended_count=len(models)
    report = {
        "problem_type": problem_type,
        "recommended_models": models,
        "recommended_count": recommended_count
    }
    return report