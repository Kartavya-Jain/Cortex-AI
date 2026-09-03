from ml.preprocessing.duplicates import handle_duplicates
from ml.preprocessing.missing import handle_missing_values
from ml.preprocessing.constant_columns import handle_constant_columns
from ml.preprocessing.datatypes import handle_datatypes
from ml.preprocessing.outliers import handle_outliers
from ml.preprocessing.high_cardinality import handle_high_cardinality
from ml.preprocessing.encoding import handle_encoding
from ml.preprocessing.scaling import handle_scaling
def preprocess_dataset(df, target_column=None):
    """
    Automatically do preprocessing
    """

    df, duplicates_preprocessing_report=handle_duplicates(df)
    print("AFTER DUPLICATES:", df[target_column].value_counts(dropna=False).to_dict())
    df, missing_preprocessing_report=handle_missing_values(df)
    print("AFTER MISSING:", df[target_column].value_counts(dropna=False).to_dict())
    df, constant_columns_preprocessing_report=handle_constant_columns(df)
    print("AFTER CONSTANT:", df[target_column].value_counts(dropna=False).to_dict())
    df, datatypes_preprocessing_report=handle_datatypes(df)
    print("AFTER DATATYPES:", df[target_column].value_counts(dropna=False).to_dict())
    df, outliers_preprocessing_report=handle_outliers(df, target_column=target_column)
    print("AFTER OUTLIERS:", df[target_column].value_counts(dropna=False).to_dict())
    df, high_cardinality_preprocessing_report=handle_high_cardinality(df)
    print("AFTER HIGH CARDINALITY:", df[target_column].value_counts(dropna=False).to_dict())
    df, encoding_preprocessing_report=handle_encoding(df)
    print("AFTER ENCODING:", df[target_column].value_counts(dropna=False).to_dict())
    df, scaling_preprocessing_report=handle_scaling(df, target_column=target_column)
    print("AFTER SCALING:", df[target_column].value_counts(dropna=False).to_dict())
    preprocessing_artifacts = {
        "frequency_maps": high_cardinality_preprocessing_report["frequency_maps"],
        "scaler": scaling_preprocessing_report["scaler"],
        "encoded_columns": encoding_preprocessing_report["encoded_columns"]
    }
    report = {
    "duplicates_preprocessing": duplicates_preprocessing_report,
    "missing_preprocessing": missing_preprocessing_report,
    "constant_columns_preprocessing": constant_columns_preprocessing_report,
    "datatypes_preprocessing": datatypes_preprocessing_report,
    "outliers_preprocessing": outliers_preprocessing_report,
    "high_cardinality_preprocessing": high_cardinality_preprocessing_report,
    "encoding_preprocessing": encoding_preprocessing_report,
    "scaling_preprocessing": scaling_preprocessing_report,
    "artifacts": preprocessing_artifacts
    }
    return df, report