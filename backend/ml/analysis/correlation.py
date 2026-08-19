def analyze_correlation(df):
    numeric_columns=df.select_dtypes(include="number").columns
    correlation_matrix=df[numeric_columns].corr().to_dict()
    report = {
        "correlation_matrix": correlation_matrix
    }
    return report