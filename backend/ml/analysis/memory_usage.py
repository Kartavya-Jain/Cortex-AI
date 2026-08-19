def analyze_memory_usage(df):
    memory_usage = (
        df.memory_usage(deep=True)/(1024**2)
    ).round(4)
    total_memory_mb=round(memory_usage.sum(),4)
    column_memory_mb=memory_usage.to_dict()
    report = {
        "total_memory_mb": total_memory_mb,
        "column_memory_mb":column_memory_mb
    }
    return report