def select_best_model(models):
    if not models:
        return None, {
            "best_model": None,
            "best_score": None
        }
    best_model=max(models,key=lambda x:x.get("score", float("-inf")))
    report = {
        "best_model": best_model["model_name"],
        "best_score": round(best_model["score"],4)
    }
    return best_model, report