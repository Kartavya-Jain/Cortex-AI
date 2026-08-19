from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
def handle_scaling(df, strategy="minmax"):
    numeric_columns=df.select_dtypes(include="number").columns
    if strategy=="minmax":
        scaler=MinMaxScaler()
        df[numeric_columns]=scaler.fit_transform(df[numeric_columns])
    elif strategy=="standard":
        scaler=StandardScaler()
        df[numeric_columns]=scaler.fit_transform(df[numeric_columns])
    scaled_count=len(numeric_columns)
    report = {
        "strategy": strategy,
        "scaled_columns": list(numeric_columns),
        "scaled_count": scaled_count
    }
    return df, report