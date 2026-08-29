def select_best_model(trained_models, evaluation_results, problem_type):
    if problem_type == "regression":
        best_name = max(
            evaluation_results,
            key=lambda name:evaluation_results[name]["R2"]
        )
    elif problem_type == "classification":
        best_name = max(
            evaluation_results,
            key=lambda name:evaluation_results[name]["f1"]
        )
    else:
        raise ValueError(
            f"Unsupported problem type: {problem_type}"
        )
    best_model = trained_models[best_name]
    return best_name, best_model