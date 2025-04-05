from typing import Union
import pandas as pd
from io import StringIO, BytesIO

from cleaner.exporters import EXPORTERS

def export_dataframe(df: pd.DataFrame, file_format: str) -> Union[StringIO, BytesIO]:
    """
    Exporta un DataFrame al formato solicitado usando los exporters disponibles.
    
    :param df: DataFrame limpio a exportar.
    :param file_format: Formato deseado ('csv', 'tsv', 'xlsx', 'json', 'parquet').
    :return: Objeto StringIO o BytesIO con el contenido exportado.
    """
    exporter = EXPORTERS.get(file_format.lower())
    if not exporter:
        raise ValueError(f"Formato de exportación '{file_format}' no soportado.")
    
    return exporter(df)
