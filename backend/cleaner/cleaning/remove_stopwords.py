import pandas as pd
import nltk
from nltk.corpus import stopwords

# Descargar solo si no están disponibles
try:
    stop_words = set(stopwords.words("spanish")) | set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("spanish")) | set(stopwords.words("english"))

def remove_stopwords(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina palabras vacías (stopwords) de columnas tipo string.
    """
    def clean_text(s):
        if not isinstance(s, str):
            return s
        return " ".join([word for word in s.split() if word.lower() not in stop_words])

    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].map(clean_text)
    return df
