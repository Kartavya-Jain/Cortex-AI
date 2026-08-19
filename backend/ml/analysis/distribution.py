from ml.analysis.skewness import analyze_skewness
def analyze_distribution(df):
    skewness_report=analyze_skewness(df)
    distribution={}
    for columns, value in skewness_report["skewness"].items():
        if -0.5 <= value <= 0.5:
            distribution[columns]="Approximately Normal"
        elif 0.5 < value <= 1:
            distribution[columns]="Moderately Positively Skewed"
        elif -1 <= value < -0.5:
            distribution[columns]="Moderately Negatively Skewed"
        elif value > 1:
            distribution[columns]="Highly Positively Skewed"
        else:
            distribution[columns]="Highly Negatively Skewed"
    report = {
        "distribution": distribution
    }
    return report