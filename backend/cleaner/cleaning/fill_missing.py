import pandas as pd

def fill_missing_values(df: pd.DataFrame, value="N/A") -> pd.DataFrame:
    """
    Rellena valores nulos con un valor por defecto. Por defecto: 'N/A'
    """
    return df.fillna(value)
