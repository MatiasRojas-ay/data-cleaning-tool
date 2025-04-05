from cleaner.readers import (
    detect_file_type,
    read_csv,
    read_tsv,
    read_excel,
    read_json,
    read_parquet,
)

def process_uploaded_file(file):
    file_type = detect_file_type(file.name)

    if file_type == "csv":
        return read_csv(file)
    elif file_type == "tsv":
        return read_tsv(file)
    elif file_type == "excel":
        return read_excel(file)
    elif file_type == "json":
        return read_json(file)
    elif file_type == "parquet":
        return read_parquet(file)
    else:
        raise ValueError("Formato de archivo no soportado")
