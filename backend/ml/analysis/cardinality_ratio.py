def analyze_cardinality_ratio(df):
    total_rows=len(df)
    cardinality_ratio={}
    for column in df.select_dtypes(include=["object","category"]).columns:
        unique_count=df[column].nunique(dropna=False)
        ratio=round(unique_count/total_rows,4)
        cardinality_ratio[column]={
            "unique_count": unique_count,
            "cardinality_ratio": ratio
        }
    report = {
        "categorical_columns": len(cardinality_ratio),
        "cardinality": cardinality_ratio
    }
    return report