from rest_framework import serializers
from cleaner.services.cleaning_service import CLEANING_FUNCTIONS

EXPORT_FORMATS = ["csv", "tsv", "xlsx", "json", "parquet"]
CLEANING_OPERATIONS = list(CLEANING_FUNCTIONS.keys())

class CleanFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    format = serializers.ChoiceField(choices=EXPORT_FORMATS, default="csv")
    operations = serializers.ListField(
        child=serializers.ChoiceField(choices=CLEANING_OPERATIONS),
        required=False,
        default=[]
    )