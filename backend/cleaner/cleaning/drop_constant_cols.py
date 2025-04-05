import pandas as pd

def remove_constant_cols(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina columnas con un solo valor (sin variación).
    """
    return df.loc[:, df.nunique() > 1]
