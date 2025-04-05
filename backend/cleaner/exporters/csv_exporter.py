import pandas as pd
from io import StringIO

def export_to_csv(df: pd.DataFrame) -> StringIO:
    """
    Exporta un DataFrame a un objeto StringIO como CSV.
    """
    buffer = StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    return buffer
