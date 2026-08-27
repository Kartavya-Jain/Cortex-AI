def analyze_column_roles(df):
    id_columns=[]
    feature_columns=[]
    target_column=None
    target_type=None
    for column in df.columns:
        column_name=column.lower()
        if (
            "id" in column_name
            or "index" in column_name
            or df[column].nunique(dropna=False)==len(df)
        ):
            id_columns.append(column)
        non_id_columns = [
            column for column in df.columns
            if column not in id_columns
        ]
        if non_id_columns:
            candidate = non_id_columns[-1]
            unique_count = df[candidate].nunique(dropna=False)
            if df[candidate].dtype == "object" or unique_count<=20:
                target_column=candidate
                target_type="classification"
            elif df[candidate].dtype in ["int64", "float64"]:
                target_column=candidate
                target_type="regression"
        feature_columns=[
            column
            for column in df.columns
            if column not in id_columns
            and column!=target_column]
    report = {
        "id_columns": id_columns,
        "target_column": target_column,
        "target_type": target_type,
        "feature_columns": feature_columns
    }
    return report
def detect_target_type(df, target_column):
    if target_column is None:
        return None
    if target_column not in df.columns:
        return None
    if df[target_column].dtype == "object" or df[target_column].dtype.name == "category":
        return "classification"
    if df[target_column].dtype == "bool":
        return "classification"
    if df[target_column].dtype in ["int64", "int32", "float64", "float32"]:
        unique_count = df[target_column].nunique(dropna=True)
        if unique_count <= 10:
            return "classification"
        return "regression"
    return None