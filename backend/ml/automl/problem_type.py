from ml.automl.target_detection import detect_target
from pandas.api.types import is_numeric_dtype
def detect_problem_type(df):
    target_report=detect_target(df)
    target_column=target_report["target_column"]
    target=df[target_column]
    unique_count=target.nunique()
    if not is_numeric_dtype(target):
        problem_type="classification"
    elif unique_count <= 20:
        problem_type="classification"
    else:
        problem_type="regression"
    report = {
        "target_column": target_column,
        "problem_type": problem_type,
        "unique_values": unique_count
    }
    return report