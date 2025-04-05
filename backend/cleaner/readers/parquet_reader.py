import pandas as pd
from typing import IO

def read_parquet(file: IO) -> pd.DataFrame:
    try:
        df = pd.read_parquet(file)
        return df
    except Exception as e:
        raise ValueError(f"Error al leer Parquet: {e}")
