import os

def detect_file_type(filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()
    if ext == ".csv":
        return "csv"
    elif ext in [".tsv", ".tab"]:
        return "tsv"
    elif ext in [".xls", ".xlsx"]:
        return "excel"
    elif ext == ".json":
        return "json"
    elif ext == ".parquet":
        return "parquet"
    else:
        raise ValueError("Formato de archivo no soportado")
