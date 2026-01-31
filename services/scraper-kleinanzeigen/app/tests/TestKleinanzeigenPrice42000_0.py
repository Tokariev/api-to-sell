import unittest
import os
from app.KleinanzeigenScraper import KleinanzeigenScraper

URL = "https://www.ebay-kleinanzeigen.de/s-anzeige/2324472366"
MOCK_DIR = os.path.join(os.path.dirname(__file__), '..', 'mock')


class TestMobileSvcScraper(unittest.TestCase):
    def setUp(self):
        mock_file = os.path.join(MOCK_DIR, 'kleinanzeige_price_420000.json')
        with open(mock_file, 'r', encoding="utf-8") as file:
            mock_page_content = file.read()

        self.scraper = KleinanzeigenScraper(
            URL, page_content=mock_page_content)


    def test_get_price(self):
        # Current price 42000.0
        exp = 42000
        act = self.scraper.get_price()
        self.assertEqual(exp, act, "Price not found")
