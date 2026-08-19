def analyze_constant_columns(df):
    constant_columns=[]
    for x in df.columns:
        if df[x].nunique()==1:
            constant_columns.append(x)
    constant_columns_count=len(constant_columns)
    report = {
        "constant_columns": constant_columns,
        "constant_columns_count": constant_columns_count
    }
    return report