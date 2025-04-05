import pandas as pd
from django.test import TestCase
from cleaner.services.exporter_service import export_dataframe
import json

class ExporterServiceTest(TestCase):
    def setUp(self):
        self.df = pd.DataFrame({"a": [1, 2], "b": ["x", "y"]})

    def test_export_to_csv(self):
        output = export_dataframe(self.df, "csv")
        content = output.getvalue().decode("utf-8")
        self.assertIn("a,b", content)
        self.assertIn("1,x", content)

    def test_export_to_tsv(self):
        output = export_dataframe(self.df, "tsv")
        content = output.getvalue()  # ahora sí es StringIO
        self.assertIn("a\tb", content)
        self.assertIn("1\tx", content)

    def test_export_to_excel(self):
        output = export_dataframe(self.df, "xlsx")
        self.assertTrue(output.read(4).startswith(b"PK"))  # .xlsx is zipped

    def test_export_to_json(self):
        output = export_dataframe(self.df, "json")
        content = json.loads(output.getvalue())
        self.assertEqual(content[0]["a"], 1)
        self.assertEqual(content[0]["b"], "x")

    def test_export_to_parquet(self):
        output = export_dataframe(self.df, "parquet")
        self.assertTrue(output.read(4))  # No assert de contenido directo (binario), solo que exista
