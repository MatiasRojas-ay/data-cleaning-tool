from rest_framework.test import APITestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.datastructures import MultiValueDict
import os


class CleanFileViewTest(APITestCase):
    def test_clean_csv_file_and_download_csv(self):
        # Usar el archivo CSV real de fixtures
        path = os.path.join(os.path.dirname(__file__), "fixtures", "sample.csv")
        with open(path, "rb") as f:
            uploaded_file = SimpleUploadedFile("sample.csv", f.read(), content_type="text/csv")

        url = reverse("clean-file")

        data = MultiValueDict({
            "file": [uploaded_file],
            "format": ["csv"],
            "operations": ["remove_empty_rows", "drop_duplicate_rows"],
        })

        response = self.client.post(url, data, format="multipart")

        try:
            content = b"".join(response.streaming_content)
        except Exception as e:
            self.fail(f"Fallo al leer streaming_content: {e}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/csv")
        self.assertIn(b"name,age", content)
        self.assertIn(b"Alice,30", content)

    def test_invalid_format(self):
        path = os.path.join(os.path.dirname(__file__), "fixtures", "sample.csv")
        with open(path, "rb") as f:
            file = SimpleUploadedFile("sample.csv", f.read(), content_type="text/csv")
        response = self.client.post(
            "/api/clean/",
            {
                "file": file,
                "format": "exe",  # inválido
                "operations": ["normalize_text"],
            },
            format="multipart",
        )
        self.assertEqual(response.status_code, 400)
