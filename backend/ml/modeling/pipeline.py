from ml.analysis.column_roles import analyze_column_roles
from ml.preprocessing.preprocess import preprocess_dataset

from ml.modeling.split import split_features_target
from ml.modeling.train_test import train_test_split
from ml.modeling.models import get_models
from ml.modeling.train_models import train_models
from ml.modeling.evaluate_models import evaluate_models
from ml.modeling.select_best import select_best_model
from ml.modeling.model_storage import save_model
import joblib
from pathlib import Path

def run_ml_pipeline(df):
    #1. Detect target
    roles = analyze_column_roles(df)
    target_column = roles["target_column"]
    problem_type = roles["target_type"]
    if target_column is None:
        raise ValueError("Target column couldn't be detected.")
    #2. Preprocesing
    cleaned_df, preprocessing_info = preprocess_dataset(df, target_column)
    ARTIFACT_PATH = Path(__file__).resolve().parent.parent / "saved_models"/"preprocessing_artifacts.pkl"
    joblib.dump(
        preprocessing_info["artifacts"],
        ARTIFACT_PATH
    )
    #3. Feature / Target split
    X, y, split_info = split_features_target(
        cleaned_df,
        target_column
    )
    #4. Train / Test split
    X_train, X_test, y_train, y_test, split_report = train_test_split(
        X,
        y
    )
    #5. Get models
    models = get_models(problem_type)
    #6. Train
    trained_models, training_info = train_models(
        models,
        X_train,
        y_train
    )
    #7. Evaluate
    evaluation_results = evaluate_models(
        trained_models,
        X_test,
        y_test,
        problem_type
    )
    #8. Select best
    best_name, best_model = select_best_model(
        trained_models,
        evaluation_results,
        problem_type
    )
    #9. Save best model
    model_info = save_model(best_model)

    #10. Save feature columns
    BASE_DIR = Path(__file__).resolve().parent.parent
    FEATURE_PATH = BASE_DIR / "saved_models"/"feature_columns.pkl"
    joblib.dump(X.columns.tolist(), FEATURE_PATH)
    return {
        "target_column": target_column,
        "problem_type": problem_type,
        "preprocessing": preprocessing_info,
        "feature_target_split": split_info,
        "train_test_split": split_report,
        "training": training_info,
        "evaluation": evaluation_results,
        "best_model": best_name,
        "model_storage": model_info
    }