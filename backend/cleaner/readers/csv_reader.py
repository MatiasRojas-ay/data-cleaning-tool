import pandas as pd
from typing import IO

def read_csv(file: IO) -> pd.DataFrame:
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        raise ValueError(f"Error al leer CSV: {e}")
