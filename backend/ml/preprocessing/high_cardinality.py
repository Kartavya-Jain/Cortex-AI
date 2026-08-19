from ml.analysis.high_cardinality import analyze_high_cardinality
def handle_high_cardinality(df):
    high_cardinality_report=analyze_high_cardinality(df)
    high_cardinality_columns=high_cardinality_report["high_cardinality_columns"]
    for column in high_cardinality_columns:
        frequency=df[column].value_counts()
        df[column]=df[column].map(frequency)
    report = {
        "handled_columns": high_cardinality_columns,
        "handled_count": len(high_cardinality_columns),
        "encoding_method": "frequency_encoding"
    }
    return df, report