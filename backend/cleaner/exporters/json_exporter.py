import pandas as pd
from io import StringIO
import json

def export_to_json(df: pd.DataFrame) -> StringIO:
    """
    Exporta un DataFrame como JSON a un StringIO.
    """
    buffer = StringIO()
    json.dump(json.loads(df.to_json(orient='records')), buffer, indent=2)
    buffer.seek(0)
    return buffer
