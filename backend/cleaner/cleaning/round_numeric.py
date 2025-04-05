import pandas as pd

def round_numeric(df: pd.DataFrame, decimals=2) -> pd.DataFrame:
    """
    Redondea valores numéricos a la cantidad de decimales especificada.
    """
    return df.round(decimals)
