from ml.analysis.datatypes import analyze_datatypes
import pandas as pd
def handle_datatypes(df):
    datatype_report=analyze_datatypes(df)
    object_columns=datatype_report["object_columns"]
    converted_columns=[]
    for column in object_columns:
        converted=pd.to_numeric(df[column], errors="coerce")
        if converted.notna().sum()==len(df):
            df[column]=converted
            converted_columns.append(column)
    converted_count=len(converted_columns)
    report = {
        "converted_columns": converted_columns,
        "converted_count": converted_count
    }
    return df, report