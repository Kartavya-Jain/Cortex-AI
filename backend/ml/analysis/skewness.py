def analyze_skewness(df):
    numeric_columns=df.select_dtypes(include="number").columns
    skewness=df[numeric_columns].skew().to_dict()
    report ={
        "skewness": skewness
    }
    return report