import pandas as pd
from io import BytesIO

def export_to_excel(df: pd.DataFrame) -> BytesIO:
    """
    Exporta un DataFrame a un objeto BytesIO como Excel.
    """
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    buffer.seek(0)
    return buffer
