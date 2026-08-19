import pandas as pd
def profile_dataset(file_path):
    df=pd.read_csv(file_path)
    rows= df.shape[0]
    columns= df.shape[1]
    column_names= df.columns.tolist()
    missing_values= df.isnull().sum().to_dict()
    duplicated_values= int(df.duplicated().sum())
    data_types= df.dtypes.astype(str).to_dict()
    numeric_columns= df.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns= df.select_dtypes(include=["object"]).columns.tolist()
    memory_usage_mb= round(df.memory_usage(deep=True).sum()/1024/1024,2)
    unique_values= df.nunique().to_dict()
    total_missing_values=int(df.isnull().sum().sum())
    columns_with_missing_values=int((df.isnull().sum()>0).sum())
    numeric_columns_count=len(numeric_columns)
    categorical_columns_count=len(categorical_columns)
    missing_percentage=((df.isnull().sum()/len(df))*100).round(2).to_dict()
    constant_columns=[
        col
        for col in df.columns
        if df[col].nunique()==1
    ]
    high_cardinality_columns=[
        col
        for col in df.select_dtypes(include="object").columns
        if df[col].nunique()>100
    ]
    dataset_score=100
    highest_missing_percentage=max(missing_percentage.values())
    if highest_missing_percentage>30:
        dataset_score-=20
    elif highest_missing_percentage>15:
        dataset_score-=10
    elif highest_missing_percentage>5:
        dataset_score-=5
    duplicate_percentage=(duplicated_values/rows)*100
    if duplicate_percentage>5:
        dataset_score-=10
    elif duplicate_percentage>1:
        dataset_score-=5
    elif duplicate_percentage>0:
        dataset_score-=2
    dataset_score-=len(constant_columns)*5
    dataset_score-=min(len(high_cardinality_columns)*2,10)
    dataset_score=max(dataset_score,0)
    if dataset_score>=90:
        dataset_status="Excellent"
    elif dataset_score>=75:
        dataset_status="Good"
    elif dataset_score>50:
        dataset_status="Needs Cleaning"
    else:
        dataset_status="Poor"
    return {
        "rows": rows,
        "columns": columns,
        "column_names": column_names,
        "missing_values": missing_values,
        "duplicated_values": duplicated_values,
        "data_types": data_types,
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "memory_usage_mb": memory_usage_mb,
        "unique_values": unique_values,
        "total_missing_values": total_missing_values,
        "columns_with_missing_values": columns_with_missing_values,
        "numeric_columns_count": numeric_columns_count,
        "categorical_columns_count": categorical_columns_count,
        "missing_percentage": missing_percentage,
        "constant_columns": constant_columns,
        "high_cardinality_columns": high_cardinality_columns,
        "dataset_health": {
            "score": dataset_score,
            "status": dataset_status
        }
    }