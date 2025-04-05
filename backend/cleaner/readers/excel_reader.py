import pandas as pd
from typing import IO

def read_excel(file: IO) -> pd.DataFrame:
    try:
        df = pd.read_excel(file)
        return df
    except Exception as e:
        raise ValueError(f"Error al leer Excel: {e}")