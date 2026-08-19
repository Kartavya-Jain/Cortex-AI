from ml.analysis.outliers import analyze_outliers
def handle_outliers(df, strategy="cap"):
    outliers_report=analyze_outliers(df)
    outliers=outliers_report["outliers"]
    handled_columns=[]
    if strategy=="cap":
        for column, values in outliers.items():
            lower_bound=values["lower_bound"]
            upper_bound=values["upper_bound"]
            df[column]=df[column].clip(
                lower=lower_bound,
                upper=upper_bound
            )
            handled_columns.append(column)
    handled_count=len(handled_columns)
    report = {
        "strategy": strategy,
        "handled_columns": handled_columns,
        "handled_count": handled_count
    }
    return df, report