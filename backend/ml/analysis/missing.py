def analyze_missing_values(df):
    missing_count={}
    missing_percentage={}
    for x in df.columns:
        missing_count[x] = int(df[x].isnull().sum())
        missing_percentage[x] = round(df[x].isnull().sum()*100/ len(df),2)
    report = {
        "missing_count": missing_count,
        "missing_percentage":missing_percentage
    }
    return report