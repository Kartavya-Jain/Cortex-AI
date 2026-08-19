from ml.analysis.datatypes import analyze_datatypes
from ml.analysis.high_cardinality import analyze_high_cardinality
import pandas as pd
def handle_encoding(df):
    datatype_report=analyze_datatypes(df)
    high_cardinality_report=analyze_high_cardinality(df)
    object_columns=datatype_report["object_columns"]
    high_cardinality_columns=high_cardinality_report["high_cardinality_columns"]
    columns_to_encode=[]
    for column in object_columns:
        if column not in high_cardinality_columns:
            columns_to_encode.append(column)
    df=pd.get_dummies(df, columns=columns_to_encode, drop_first=True)
    encoded_count=len(columns_to_encode)
    report = {
        "encoding_method": "one-hot",
        "encoded_columns": columns_to_encode,
        "encoded_count": encoded_count
    }
    return df, report