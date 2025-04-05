import pandas as pd

def remove_numeric_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina filas que contienen solo valores numéricos (útil para limpiar textos mal formateados).
    """
    return df[~df.apply(lambda row: all(isinstance(x, (int, float)) for x in row), axis=1)]
