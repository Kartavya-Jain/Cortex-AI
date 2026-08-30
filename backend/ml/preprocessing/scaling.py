from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import joblib
from pathlib import Path
def handle_scaling(df, strategy="minmax", target_column=None):
    numeric_columns=df.select_dtypes(include="number").columns.tolist()
    if target_column in numeric_columns:
         numeric_columns.remove(target_column)
    if len(numeric_columns) == 0:
        report = {
            "strategy": strategy,
            "scaled_columns": [],
            "scaled_count": 0
        }
        return df, report
    if strategy=="minmax":
        scaler=MinMaxScaler()
        df[numeric_columns]=scaler.fit_transform(df[numeric_columns])
    elif strategy=="standard":
        scaler=StandardScaler()
        df[numeric_columns]=scaler.fit_transform(df[numeric_columns])
    BASE_DIR = Path(__file__).resolve().parent.parent
    joblib.dump(
        scaler,
        BASE_DIR / "saved_models" / "scaler.pkl"
    )
    scaled_count=len(numeric_columns)
    report = {
        "strategy": strategy,
        "scaled_columns": list(numeric_columns),
        "scaled_count": scaled_count,
        "scaler": scaler
    }
    return df, report