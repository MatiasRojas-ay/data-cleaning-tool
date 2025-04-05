import pandas as pd
from typing import IO

def read_tsv(file: IO) -> pd.DataFrame:
    try:
        df = pd.read_csv(file, sep='\t')
        return df
    except Exception as e:
        raise ValueError(f"Error al leer TSV: {e}")
