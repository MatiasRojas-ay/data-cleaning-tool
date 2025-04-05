from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse

from .serializers import CleanFileSerializer
from cleaner.services.reader_service import process_uploaded_file
from cleaner.services.cleaning_service import apply_cleaning_operations
from cleaner.services.exporter_service import export_dataframe


class CleanFileView(APIView):
    """
    Endpoint que permite subir un archivo, aplicar funciones de limpieza y devolver el resultado en el formato deseado.
    """

    def post(self, request, format=None):
        serializer = CleanFileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        file = serializer.validated_data["file"]
        operations = serializer.validated_data.get("operations", [])
        export_format = serializer.validated_data["format"]

        try:
            # 1. Leer archivo
            df = process_uploaded_file(file)

            # 2. Aplicar funciones de limpieza
            df = apply_cleaning_operations(df, operations)

            # 3. Exportar resultado
            exported_file = export_dataframe(df, export_format)

        except Exception as e:
            print("💥 Error interno:", str(e))  # ⬅️ esto te dirá si algo se rompe en cleaning/exporting
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # 4. Enviar archivo como respuesta
        filename = f"archivo_limpio.{export_format}"
        content_type = {
            "csv": "text/csv",
            "tsv": "text/tab-separated-values",
            "json": "application/json",
            "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "parquet": "application/octet-stream",
        }.get(export_format, "application/octet-stream")

        return FileResponse(exported_file, as_attachment=True, filename=filename, content_type=content_type)
