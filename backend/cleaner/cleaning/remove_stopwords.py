import pandas as pd
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
stop_words = set(stopwords.words('spanish')) | set(stopwords.words('english'))

def remove_stopwords(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina palabras vacías (stopwords) de columnas tipo string.
    """
    def clean_text(s):
        if not isinstance(s, str):
            return s
        return " ".join([word for word in s.split() if word.lower() not in stop_words])
    
    return df.applymap(clean_text)
