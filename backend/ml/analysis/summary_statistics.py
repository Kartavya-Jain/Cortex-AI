def analyze_summary_statistics(df):
    statistics=df.describe()
    report = {
        "statistics": statistics
    }
    return report