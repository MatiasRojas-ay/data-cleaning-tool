from typing import List, Callable
import pandas as pd

from cleaner.cleaning import (
    drop_empty_columns,
    remove_empty_rows,
    drop_duplicate_rows,
    remove_constant_cols,
    remove_high_null_cols,
    drop_outliers,
    fill_missing_values,
    strip_whitespace,
    remove_special_chars,
    remove_numeric_rows,
    remove_stopwords,
    standardize_columns,
    convert_dtypes,
    parse_dates,
    round_numeric,
    normalize_text,
)

# Diccionario que mapea strings (elegidas por el usuario) a funciones reales
CLEANING_FUNCTIONS: dict[str, Callable[[pd.DataFrame], pd.DataFrame]] = {
    "drop_empty_columns": drop_empty_columns,
    "remove_empty_rows": remove_empty_rows,
    "drop_duplicate_rows": drop_duplicate_rows,
    "remove_constant_cols": remove_constant_cols,
    "remove_high_null_cols": remove_high_null_cols,
    "drop_outliers": drop_outliers,
    "fill_missing_values": fill_missing_values,
    "strip_whitespace": strip_whitespace,
    "remove_special_chars": remove_special_chars,
    "remove_numeric_rows": remove_numeric_rows,
    "remove_stopwords": remove_stopwords,
    "standardize_columns": standardize_columns,
    "convert_dtypes": convert_dtypes,
    "parse_dates": parse_dates,
    "round_numeric": round_numeric,
    "normalize_text": normalize_text,
}

def apply_cleaning_operations(df: pd.DataFrame, operations: List[str]) -> pd.DataFrame:
    """
    Aplica una lista de operaciones de limpieza al DataFrame.
    Las operaciones deben ser claves del diccionario CLEANING_FUNCTIONS.
    """
    for op in operations:
        func = CLEANING_FUNCTIONS.get(op)
        if not func:
            print(f"⚠️  Operación desconocida: {op}")
            continue
        try:
            df = func(df)
        except Exception as e:
            print(f"⚠️  Error al aplicar '{op}': {e}")
            continue
    return df
