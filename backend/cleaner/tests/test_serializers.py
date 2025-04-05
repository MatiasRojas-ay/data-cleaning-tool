from django.test import TestCase
from cleaner.serializers import CleanFileSerializer


class CleanFileSerializerTest(TestCase):
    def test_invalid_without_file(self):
        data = {
            "format": "csv",
            "operations": ["normalize_text", "round_numeric"],
        }
        serializer = CleanFileSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("file", serializer.errors)

    def test_valid_with_minimal_data(self):
        from django.core.files.uploadedfile import SimpleUploadedFile

        file = SimpleUploadedFile("test.csv", b"col1,col2\n1,2", content_type="text/csv")
        data = {
            "file": file,
            "format": "csv",
            "operations": [],
        }
        serializer = CleanFileSerializer(data=data)
        self.assertTrue(serializer.is_valid())
