import pandas as pd
from io import BytesIO

def export_to_csv(df: pd.DataFrame) -> BytesIO:
    """
    Exporta un DataFrame a CSV codificado en UTF-8 como BytesIO.
    Esto es compatible con FileResponse de Django.
    """
    buffer = BytesIO()
    df.to_csv(buffer, index=False, encoding='utf-8')
    buffer.seek(0)
    return buffer
