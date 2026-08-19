from ml.analysis.duplicates import analyze_duplicates
def handle_duplicates(df):
    duplicate_report=analyze_duplicates(df)
    duplicate_count=duplicate_report["duplicate_count"]
    duplicate_percentage=duplicate_report["duplicate_percentage"]
    df=df.drop_duplicates().copy()
    report = {
        "removed_duplicates": duplicate_count,
        "removed_percentage": duplicate_percentage,
        "remaining_duplicates": 0
    }
    return df, report