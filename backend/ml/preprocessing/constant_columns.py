from ml.analysis.constant_columns import analyze_constant_columns
def handle_constant_columns(df):
    constant_columns_report=analyze_constant_columns(df)
    constant_columns=constant_columns_report["constant_columns"]
    if constant_columns:
        df=df.drop(columns=constant_columns, errors="ignore")
    removed_count=len(constant_columns)
    report = {
        "removed_columns": constant_columns,
        "removed_count": removed_count
    }
    return df, report