import pandas as pd
import re

def remove_special_chars(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina caracteres especiales de las columnas de texto.
    """
    return df.applymap(lambda x: re.sub(r'[^\w\s]', '', x) if isinstance(x, str) else x)
