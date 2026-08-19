def select_low_variance_features(df, threshold=0.01):
    numeric_columns=df.select_dtypes(include="number").columns
    variance=df["numeric_columns"].var()
    low_variance_columns = variance[variance<threshold].index.tolist()
    low_variance_count=len(low_variance_columns)
    report = {
        "threshold": threshold,
        "low_variance_columns": low_variance_columns,
        "low_variance_count": low_variance_count
    }
    return report