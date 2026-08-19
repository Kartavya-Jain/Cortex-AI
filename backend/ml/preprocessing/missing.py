def handle_missing_values(df, numeric_strategy="median", categorical_strategy="mode"):
    missing_before=int(df.isnull().sum().sum())
    numeric_columns=df.select_dtypes(include="number").columns
    categorical_columns=df.select_dtypes(include="object").columns
    if numeric_strategy=="mean":
        for x in numeric_columns:
            df[x]=df[x].fillna(df[x].mean())
    elif numeric_strategy=="median":
        for x in numeric_columns:
            df[x]=df[x].fillna(df[x].median())
    if categorical_strategy=="mode":
        for x in categorical_columns:
            df[x]=df[x].fillna(df[x].mode()[0])
    missing_after=int(df.isnull().sum().sum())
    report = {
        "strategy": {
            "numeric": numeric_strategy,
            "categorical": categorical_strategy
        },
        "missing_before": missing_before,
        "missing_after": missing_after
        }
    return df, report