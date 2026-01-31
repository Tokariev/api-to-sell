import unittest
import os
from app.KleinanzeigenScraper import KleinanzeigenScraper

URL = "https://www.ebay-kleinanzeigen.de/s-anzeige/2324472366"
MOCK_DIR = os.path.join(os.path.dirname(__file__), '..', 'mock')


class TestMobileSvcScraper(unittest.TestCase):
    def setUp(self):
        mock_file = os.path.join(MOCK_DIR, 'kleinanzeige_hidden_phone.json')
        with open(mock_file, 'r', encoding="utf-8") as file:
            mock_page_content = file.read()

        self.scraper = KleinanzeigenScraper(
            URL, page_content=mock_page_content)


    def test_get_phone_numbers(self):
        exp = ["015201497919"]
        act = self.scraper.get_seller_phones()
        self.assertEqual(exp, act, "Phone error")
