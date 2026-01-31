
import unittest
from app.ExternalCarID import ExternalCarID

class TestExternalCarID(unittest.TestCase):
    def setUp(self):
        self.extractor = ExternalCarID()

    def test_kleinanzeigen(self):
        self.assertEqual(self.extractor.extract_id_by_url("https://www.kleinanzeigen.de/s-anzeige/mazda-cx-5/2989057798-216-15355"), "2989057798")
        self.assertEqual(self.extractor.extract_id_by_url("https://www.kleinanzeigen.de/s-anzeige/kia-ceed-2012/2989058111-216-2826"), "2989058111")
        self.assertEqual(self.extractor.extract_id_by_url("https://www.kleinanzeigen.de/s-anzeige/2989058282"), "2989058282")

    def test_invalid_url(self):
        self.assertEqual(self.extractor.extract_id_by_url("https://www.example.com/no-id-here"), "Not implemented")