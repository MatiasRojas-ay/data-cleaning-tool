import pandas as pd

def strip_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """
    Quita espacios en blanco al inicio y al final de los textos en columnas tipo string.
    """
    return df.map(lambda x: x.strip() if isinstance(x, str) else x)
