import pandas as pd
from typing import IO

def read_json(file: IO) -> pd.DataFrame:
    try:
        df = pd.read_json(file)
        return df
    except Exception as e:
        raise ValueError(f"Error al leer JSON: {e}")
