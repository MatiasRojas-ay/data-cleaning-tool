import pandas as pd
from django.test import TestCase
from cleaner.cleaning import *


class CleaningServiceTest(TestCase):
    def test_drop_empty_columns(self):
        df = pd.DataFrame({"a": [1, 2], "b": [None, None]})
        cleaned = drop_empty_columns(df)
        self.assertNotIn("b", cleaned.columns)

    def test_remove_empty_rows(self):
        df = pd.DataFrame({"a": [1, None], "b": [2, None]})
        cleaned = remove_empty_rows(df)
        self.assertEqual(len(cleaned), 1)

    def test_drop_duplicate_rows(self):
        df = pd.DataFrame({"a": [1, 1], "b": ["x", "x"]})
        cleaned = drop_duplicate_rows(df)
        self.assertEqual(len(cleaned), 1)

    def test_remove_constant_cols(self):
        df = pd.DataFrame({"a": [1, 1, 1], "b": [1, 2, 3]})
        cleaned = remove_constant_cols(df)
        self.assertNotIn("a", cleaned.columns)

    def test_remove_high_null_cols(self):
        df = pd.DataFrame({"a": [None, None, 1], "b": [1, 2, 3]})
        cleaned = remove_high_null_cols(df, threshold=0.5)
        self.assertNotIn("a", cleaned.columns)

    def test_drop_outliers(self):
        df = pd.DataFrame({"a": [100, 102, 104, 300]})
        cleaned = drop_outliers(df)
        self.assertNotIn(300, cleaned["a"].values)
        self.assertEqual(len(cleaned), 3)

    def test_fill_missing_values(self):
        df = pd.DataFrame({"a": [1, None, 3]})
        cleaned = fill_missing_values(df)
        self.assertFalse(cleaned.isnull().any().any())

    def test_strip_whitespace(self):
        df = pd.DataFrame({"a": ["  hello ", " world  "]})
        cleaned = strip_whitespace(df)
        self.assertEqual(cleaned.iloc[0]["a"], "hello")

    def test_remove_special_chars(self):
        df = pd.DataFrame({"a": ["Hello!", "W@rld#", "Te$ting%"]})
        cleaned = remove_special_chars(df)
        self.assertEqual(cleaned.iloc[1]["a"], "Wrld")

    def test_remove_numeric_rows(self):
        df = pd.DataFrame({"a": ["hello", "123", "world"]})
        cleaned = remove_numeric_rows(df)
        self.assertNotIn("123", cleaned["a"].values)
        self.assertEqual(len(cleaned), 2)

    def test_remove_stopwords(self):
        df = pd.DataFrame({"a": ["this is a test", "el perro corre"]})
        cleaned = remove_stopwords(df)
        self.assertNotIn("is", cleaned["a"].iloc[0])
        self.assertNotIn("el", cleaned["a"].iloc[1])

    def test_standardize_columns(self):
        df = pd.DataFrame({"Nombre Completo": [1], "Edad (años)": [2]})
        cleaned = standardize_columns(df)
        self.assertIn("nombre_completo", cleaned.columns)

    def test_convert_dtypes(self):
        df = pd.DataFrame({"a": ["1", "2", "3"]})
        cleaned = convert_dtypes(df)
        self.assertTrue(pd.to_numeric(cleaned["a"], errors="coerce").notna().all())

    def test_parse_dates(self):
        df = pd.DataFrame({"fecha": ["2024-01-01", "2024-05-01"]})
        cleaned = parse_dates(df)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(cleaned["fecha"]))

    def test_round_numeric(self):
        df = pd.DataFrame({"a": [1.111, 2.222, 3.333]})
        cleaned = round_numeric(df)
        self.assertEqual(cleaned["a"].iloc[0], 1.11)

    def test_normalize_text(self):
        df = pd.DataFrame({"a": ["¡Hola!", "Señor"]})
        cleaned = normalize_text(df)
        self.assertIn("senor", cleaned["a"].iloc[1])
