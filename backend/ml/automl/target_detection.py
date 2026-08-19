def detect_target(df):
    target_names = [
        "target"
        "label",
        "class",
        "output",
        "y",
        "price",
        "salary",
        "income",
        "sales",
        "survived",
        "saleprice",
        "house_price",
        "final_score"
    ]
    columns=list(df.columns)
    for column in columns:
        if column.lower() in target_names:
            return {
                "target_column": column,
                "detection_method": "column_name"
            }
    return {
        "target_column": columns[-1],
        "detection_method": "last_column"
    }