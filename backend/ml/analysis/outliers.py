import pandas as pd
def analyze_outliers(df):
    numeric_columns=df.select_dtypes(include="number").columns
    outliers={}
    for x in numeric_columns:
        Q1=df[x].quantile(0.25)
        Q3=df[x].quantile(0.75)
        IQR=Q3-Q1
        lower_bound=Q1-1.5*IQR
        upper_bound=Q3+1.5*IQR
        outlier_rows=df[(df[x]<lower_bound) | (df[x]>upper_bound)]
        outlier_count=len(outlier_rows)
        outlier_percentage=round(outlier_count*100/len(df),2)
        outliers[x] = {
            "Q1": Q1,
            "Q3":Q3,
            "IQR":IQR,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "outlier_count":outlier_count,
            "outlier_percentage": outlier_percentage
        }
    report = {
       "outliers": outliers
    }
    return report