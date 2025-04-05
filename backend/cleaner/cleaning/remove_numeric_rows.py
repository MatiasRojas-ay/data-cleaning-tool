import pandas as pd

def remove_numeric_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina filas que contienen solo valores numéricos (útil para limpiar textos mal formateados).
    """
    return df[~df.apply(lambda row: all(str(cell).isdigit() for cell in row), axis=1)]
