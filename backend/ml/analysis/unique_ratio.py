def analyze_unique_ratio(df):
    columns=df.columns
    unique_count=df[columns].nunique().to_dict()
    unique_ratio={}
    for column in unique_count:
        unique_ratio[column]=unique_count[column]/len(df)
    report = {
        "unique_count": unique_count,
        "unique_ratio": unique_ratio
    }
    return report