def analyze_variance(df):
    numeric_columns=df.select_dtypes(include="number").columns
    variance=df[numeric_columns].var().to_dict()
    report = {
        "variance": variance
    }
    return report