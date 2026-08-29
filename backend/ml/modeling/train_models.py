def train_models(models, X_train, y_train):
    trained_models = {}
    training_info = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model
        training_info[name] = {
            "status": "trained",
            "model_type": type(model).__name__
        }
    return trained_models, training_info