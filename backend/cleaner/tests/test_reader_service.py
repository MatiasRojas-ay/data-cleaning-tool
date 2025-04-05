import os
import pandas as pd
from django.test import TestCase
from cleaner.services.reader_service import process_uploaded_file
from django.core.files.uploadedfile import SimpleUploadedFile


class ReaderServiceTest(TestCase):

    def setUp(self):
        self.base_dir = os.path.join(os.path.dirname(__file__), "fixtures")

    def _load_file(self, filename, content_type):
        path = os.path.join(self.base_dir, filename)
        with open(path, "rb") as f:
            return SimpleUploadedFile(filename, f.read(), content_type=content_type)

    def test_read_csv(self):
        file = self._load_file("sample.csv", "text/csv")
        df = process_uploaded_file(file)
        self.assertEqual(df.shape[0], 4)
        self.assertIn("name", df.columns)

    def test_read_tsv(self):
        file = self._load_file("sample.tsv", "text/tab-separated-values")
        df = process_uploaded_file(file)
        self.assertEqual(df.shape[1], 3)
        self.assertIn("comment", df.columns)

    def test_read_excel(self):
        file = self._load_file("sample.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        df = process_uploaded_file(file)
        self.assertEqual(df.shape[0], 4)
        self.assertIn("age", df.columns)

    def test_read_json(self):
        file = self._load_file("sample.json", "application/json")
        df = process_uploaded_file(file)
        self.assertEqual(df.shape[1], 3)
        self.assertIn("name", df.columns)

    def test_read_parquet(self):
        file = self._load_file("sample.parquet", "application/octet-stream")
        df = process_uploaded_file(file)
        self.assertEqual(df.shape[0], 4)
        self.assertIn("age", df.columns)

    def test_invalid_extension(self):
        file = SimpleUploadedFile("sample.exe", b"fake-content", content_type="application/octet-stream")
        with self.assertRaises(ValueError):
            process_uploaded_file(file)
