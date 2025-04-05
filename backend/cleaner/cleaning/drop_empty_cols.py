import pandas as pd

def drop_empty_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina las columnas completamente vacías del DataFrame.
    """
    return df.dropna(axis=1, how='all')
