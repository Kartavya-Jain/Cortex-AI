def analyze_duplicates(df):
    duplicate_count=int(df.duplicated().sum())
    duplicate_percentage=round(duplicate_count*100/len(df),2)
    report = {
        "duplicate_count": duplicate_count,
        "duplicate_percentage":duplicate_percentage
    }
    return report