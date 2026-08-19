def analyze_feature_types(df):
    numerical_features=list(df.select_dtypes(include=["number"]).columns)
    categorical_features=list(df.select_dtypes(include=["object","category"]).columns)
    boolean_features=list(df.select_dtypes(include=["bool"]).columns)
    datetime_features=list(df.select_dtypes(include=["datetime64"]).columns)
    report = {
        "numerical_features": {
            "count": len(numerical_features),
            "columns": numerical_features
        },
        "categorical_features": {
            "count": len(categorical_features),
            "columns": categorical_features
        },
        "boolean_features": {
            "count": len(boolean_features),
            "columns": boolean_features
        },
        "datetime_features": {
            "count": len(datetime_features),
            "columns": datetime_features
        }
    }
    return report