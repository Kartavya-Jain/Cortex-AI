def analyze_null_patterns(df):
    total_rows=len(df)
    missing_columns=[]
    complete_columns=[]
    heavily_missing_columns=[]
    for column in df.columns:
        missing_count=df[column].isna().sum()
        missing_percentage=round((missing_count/total_rows)*100,2)
        if missing_count==0:
            complete_columns.append(column)
        else:
            missing_columns.append({
                "column": column,
                "missing_count": int(missing_count),
                "missing_percentage": missing_percentage
            })
            if missing_percentage>=50:
                heavily_missing_columns.append(column)
    report = {
        "missing_columns": missing_columns,
        "complete_columns": complete_columns,
        "heavily_missing_columns": heavily_missing_columns,
        "complete_column_count": len(complete_columns),
        "missing_column_count": len(missing_columns),
        "heavily_missing_count": len(heavily_missing_columns)
    }
    return report