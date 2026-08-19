def select_correlated_featues(df, threshold=0.90):
    numeric_df=df.select_dtypes(include="number")
    correlation_matrix=numeric_df.corr().abs()
    correlated_columns=set()
    columns=correlation_matrix.columns
    for i in range(len(columns)):
        for j in range(i):
            if correlation_matrix.iloc[i,j]>threshold:
                correlated_columns.add(columns[i])
    correlated_count=len(correlated_columns)
    report = {
        "correlation_threshold": threshold,
        "highly_correlated_columns": correlated_columns,
        "highly_correlated_count": correlated_count
    }
    return report