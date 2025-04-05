import pandas as pd
from io import StringIO

def export_to_tsv(df: pd.DataFrame) -> StringIO:
    """
    Exporta un DataFrame a TSV (tab-separated values) y devuelve un StringIO.
    """
    buffer = StringIO()
    df.to_csv(buffer, sep="\t", index=False)
    buffer.seek(0)
    return buffer
