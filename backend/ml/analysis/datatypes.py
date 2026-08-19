def analyze_datatypes(df):
    data_types=df.dtypes.astype(str).to_dict()
    object_columns=df.select_dtypes(include="object").columns.tolist()
    numeric_columns=df.select_dtypes(include="number").columns.tolist()
    report = {
        "data_types":data_types,
        "object_columns": object_columns,
        "numeric_columns": numeric_columns
    }
    return report