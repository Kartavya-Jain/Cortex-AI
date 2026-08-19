from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
def hyperparameter_tuning(model,X_train,y_train,problem_type):
    if problem_type=="regression":
        param_distributions = {
            "n_estimators": [100, 200, 300],
            "max_depth": [None, 10, 20, 30],
            "min_samples_split": [2, 5, 10],
            "min_samples_leaf": [1, 2, 4]
        }
    else:
        param_distributions = {
            "n_estimators": [100, 200, 300],
            "max_depth": [None, 10, 20, 30],
            "min_samples_split": [2, 5, 10],
            "min_samples_leaf": [1, 2, 4]
        }
    random_search=RandomizedSearchCV(
        estimator=model,
        param_distributions=param_distributions,
        n_iter=10,
        cv=5,
        scoring="r2" if problem_type=="regression" else "accuracy",
        random_state=42,
        n_jobs=-1
    )
    random_search.fit(X_train,y_train)
    best_model=random_search.best_estimator_
    report = {
        "problem_type": problem_type,
        "best_parameters": random_search.best_params_,
        "best_score": round(random_search.best_score_,4)
    }
    return best_model, report