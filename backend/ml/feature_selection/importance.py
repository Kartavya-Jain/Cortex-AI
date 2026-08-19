from sklearn.ensemble import RandomForestRegressor
def select_important_features(df, target_column):
    X= df.drop(columns=[target_column])
    y=df[target_column]
    model=RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X,y)
    importance=dict(
        zip(
            X.columns,
            model.feature_importances_
        )
    )
    importance = dict(
        sorted(
            importance.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )
    importance_features=list(importance.keys())
    report = {
        "target_columns": target_column,
        "feature_importance": importance,
        "importance_features": importance_features
    }
    return report