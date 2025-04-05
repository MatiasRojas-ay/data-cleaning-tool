import pandas as pd

def remove_high_null_cols(df: pd.DataFrame, threshold=0.5) -> pd.DataFrame:
    """
    Elimina columnas con un % de valores nulos superior al threshold (default 50%).
    """
    null_ratio = df.isnull().mean()
    return df.loc[:, null_ratio < threshold]
