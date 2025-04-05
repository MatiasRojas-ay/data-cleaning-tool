import pandas as pd
import re

def remove_special_chars(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina caracteres especiales de las columnas de texto.
    """
    def clean_string(x):
        return re.sub(r"[^\w\s]", "", x) if isinstance(x, str) else x

    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].map(clean_string)
    return df
