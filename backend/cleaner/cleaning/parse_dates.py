import pandas as pd

def parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Intenta convertir columnas con formato de fecha a datetime.
    """
    for col in df.columns:
        try:
            df[col] = pd.to_datetime(df[col])
        except (ValueError, TypeError):
            continue
    return df
