import pandas as pd
import numpy as np

def drop_outliers(df: pd.DataFrame, z_thresh=3) -> pd.DataFrame:
    """
    Elimina outliers usando z-score (sólo columnas numéricas).
    """
    numeric_df = df.select_dtypes(include=[np.number])
    z_scores = ((numeric_df - numeric_df.mean()) / numeric_df.std()).abs()
    mask = (z_scores < z_thresh).all(axis=1)
    return df[mask]
