import pandas as pd
import re

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renombra columnas a snake_case, sin tildes ni espacios.
    """
    def standardize(name):
        name = re.sub(r'\s+', '_', name.strip().lower())
        name = re.sub(r'[^\w_]', '', name)
        return name

    df.columns = [standardize(col) for col in df.columns]
    return df
