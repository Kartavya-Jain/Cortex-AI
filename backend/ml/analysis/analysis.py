from ml.analysis.missing import analyze_missing_values
from ml.analysis.duplicates import analyze_duplicates
from ml.analysis.datatypes import analyze_datatypes
from ml.analysis.constant_columns import analyze_constant_columns
from ml.analysis.high_cardinality import analyze_high_cardinality
from ml.analysis.outliers import analyze_outliers
from ml.analysis.correlation import analyze_correlation
from ml.analysis.skewness import analyze_skewness
from ml.analysis.summary_statistics import analyze_summary_statistics
from ml.analysis.variance import analyze_variance
from ml.analysis.unique_ratio import analyze_unique_ratio
from ml.analysis.distribution import analyze_distribution
from ml.analysis.memory_usage import analyze_memory_usage
from ml.analysis.cardinality_ratio import analyze_cardinality_ratio
from ml.analysis.class_balance import analyze_class_balance
from ml.analysis.feature_types import analyze_feature_types
from ml.analysis.null_patterns import analyze_null_patterns
from ml.analysis.column_roles import analyze_column_roles
def analyze_dataset(df):
    missing_analysis=analyze_missing_values(df)
    duplicate_analysis=analyze_duplicates(df)
    datatypes_analysis=analyze_datatypes(df)
    constant_columns_analysis=analyze_constant_columns(df)
    high_cardinality_analysis=analyze_high_cardinality(df)
    outlier_analysis=analyze_outliers(df)
    correlation_analysis=analyze_correlation(df)
    skewness_analysis=analyze_skewness(df)
    summary_statistics_analysis=analyze_summary_statistics(df)
    variance_analysis=analyze_variance(df)
    unique_ratio_analysis=analyze_unique_ratio(df)
    distribution_analysis=analyze_distribution(df)
    memory_usage_analysis=analyze_memory_usage(df)
    cardinality_ratio_analysis=analyze_cardinality_ratio(df)
    class_balance_analysis=analyze_class_balance(df)
    feature_types_analysis=analyze_feature_types(df)
    null_patterns_analysis=analyze_null_patterns(df)
    column_roles_analysis=analyze_column_roles(df)
    report = {
        "missing_analysis": missing_analysis,
        "duplicate_analysis": duplicate_analysis,
        "datatypes_analysis": datatypes_analysis,
        "constant_columns_analysis":constant_columns_analysis,
        "high_cardinality_analysis": high_cardinality_analysis,
        "outliers_analysis": outlier_analysis,
        "correlation_analysis": correlation_analysis,
        "skewness_analysis": skewness_analysis,
        "summary_statistics_analysis":summary_statistics_analysis,
        "variance_analysis": variance_analysis,
        "unique_ratio_analysis": unique_ratio_analysis,
        "distribution_analysis": distribution_analysis,
        "memory_usage_analysis": memory_usage_analysis,
        "cardinality_ratio_analysis": cardinality_ratio_analysis,
        "class_balance_analysis": class_balance_analysis,
        "feature_types_analysis": feature_types_analysis,
        "null_patterns_analysis": null_patterns_analysis,
        "column_roles_analysis": column_roles_analysis
    }
    return report