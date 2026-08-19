from ml.preprocessing.duplicates import handle_duplicates
from ml.preprocessing.missing import handle_missing_values
from ml.preprocessing.constant_columns import handle_constant_columns
from ml.preprocessing.datatypes import handle_datatypes
from ml.preprocessing.outliers import handle_outliers
from ml.preprocessing.high_cardinality import handle_high_cardinality
from ml.preprocessing.encoding import handle_encoding
from ml.preprocessing.scaling import handle_scaling
def preprocess_dataset(df):
    """
    Automatically do preprocessing
    """

    df, duplicates_preprocessing_report=handle_duplicates(df)
    df, missing_preprocessing_report=handle_missing_values(df)
    df, constant_columns_preprocessing_report=handle_constant_columns(df)
    df, datatypes_preprocessing_report=handle_datatypes(df)
    df, outliers_preprocessing_report=handle_outliers(df)
    df, high_cardinality_preprocessing_report=handle_high_cardinality(df)
    df, encoding_preprocessing_report=handle_encoding(df)
    df, scaling_preprocessing_report=handle_scaling(df) 
    report = {
    "duplicates_preprocessing": duplicates_preprocessing_report,
    "missing_preprocessing": missing_preprocessing_report,
    "constant_columns_preprocessing": constant_columns_preprocessing_report,
    "datatypes_preprocessing": datatypes_preprocessing_report,
    "outliers_preprocessing": outliers_preprocessing_report,
    "high_cardinality_preprocessing": high_cardinality_preprocessing_report,
    "encoding_preprocessing": encoding_preprocessing_report,
    "scaling_preprocessing": scaling_preprocessing_report
    }
    return df, report