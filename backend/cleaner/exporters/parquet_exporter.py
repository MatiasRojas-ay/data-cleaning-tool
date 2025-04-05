import pandas as pd
from io import BytesIO

def export_to_parquet(df: pd.DataFrame) -> BytesIO:
    buffer = BytesIO()
    df.to_parquet(buffer, index=False, engine='pyarrow')
    buffer.seek(0)
    return buffer
