from ml.automl.problem_type import detect_problem_type
from ml.automl.target_detection import detect_target
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
def train_model(df):
    target_report=detect_target(df)
    target_column=target_report["target_column"]
    X=df.drop(columns=[target_column])
    y=df[target_column]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    problem_report=detect_problem_type(df)
    problem_type=problem_report["problem_type"]
    if problem_type=="regression":
        model=RandomForestRegressor(random_state=42)
    else:
        model=RandomForestClassifier(random_state=42)
    model.fit(X_train,y_train)
    report = {
        "problem_type": problem_type,
        "model_name": model.__class__.__name__
    }
    return model, X_train, X_test, y_train, y_test, report