def analyze_high_cardinality(df):
    high_cardinality_columns=[
        col
        for col in df.select_dtypes(include="object").columns
        if df[col].nunique()>100
    ]
    high_cardinality_columns_count=len(high_cardinality_columns)
    report = {
        "high_cardinality_columns": high_cardinality_columns,
        "high_cardinality_columns_count": high_cardinality_columns_count
    }
    return report