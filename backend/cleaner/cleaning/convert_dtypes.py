import pandas as pd

def convert_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Intenta convertir las columnas a sus tipos de datos apropiados.
    """
    return df.convert_dtypes()
