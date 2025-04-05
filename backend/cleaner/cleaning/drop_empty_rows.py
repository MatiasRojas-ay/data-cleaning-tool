import pandas as pd

def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina filas completamente vacías.
    """
    return df.dropna(how='all')
