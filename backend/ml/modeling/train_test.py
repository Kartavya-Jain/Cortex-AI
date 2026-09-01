from sklearn.model_selection import train_test_split as sklearn_train_test_split
def train_test_split(X, y, test_size=0.2, random_state=42):
    stratify = y if y.value_counts().min() >= 2 else None
    X_train, X_test, y_train, y_test = sklearn_train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=stratify
    )
    report = {
        "trest_size": test_size,
        "random_state": random_state,
        "X_train_shape": X_train.shape,
        "X_test_shape": X_test.shape,
        "y_train_shape": y_train.shape,
        "y_test_shape": y_test.shape
    }
    return X_train, X_test, y_train, y_test, report