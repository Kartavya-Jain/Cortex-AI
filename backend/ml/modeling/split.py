def split_features_target(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    report = {
        "target_column": target_column,
        "feature_count": X.shape[1],
        "row_count": X.shape[0],
        "target_shape": y.shape
    }
    return X, y, report