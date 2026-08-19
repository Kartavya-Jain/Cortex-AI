from ml.automl.target_detection import detect_target
from ml.automl.problem_type import detect_problem_type
def analyze_class_balance(df):
    problem_report=detect_problem_type(df)
    if problem_report["problem_type"]!="classification":
        return {
            "Status": "Not Applicable",
            "Reason": "Dataset is Regression"
        }
    target_report=detect_target(df)
    target_column=target_report["target_column"]
    class_count=df[target_column].value_counts().to_dict()
    class_percentage = (
        (df[target_column].value_counts(normalize=True)*100).round(2).to_dict()
    )
    report = {
        "target_column": target_column,
        "class_count": class_count,
        "class_percentage": class_percentage
    }
    return report