import pandas as pd
import unicodedata

def normalize_text(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convierte texto a minúsculas, sin tildes ni caracteres especiales.
    Aplica solo a columnas de tipo 'object' (texto).
    """
    def normalize_string(s):
        if isinstance(s, str):
            nfkd_form = unicodedata.normalize('NFKD', s)
            return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()
        return s

    return df.applymap(normalize_string)
