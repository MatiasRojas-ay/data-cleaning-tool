import pandas as pd

def drop_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina filas duplicadas del DataFrame.
    """
    return df.drop_duplicates()
