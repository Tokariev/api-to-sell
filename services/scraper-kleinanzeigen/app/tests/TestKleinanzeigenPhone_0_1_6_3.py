import unittest
import os
from app.KleinanzeigenScraper import KleinanzeigenScraper

URL = "https://www.ebay-kleinanzeigen.de/s-anzeige/2324472366"
MOCK_DIR = os.path.join(os.path.dirname(__file__), '..', 'mock')


class TestMobileSvcScraper(unittest.TestCase):
    def setUp(self):
        mock_file = os.path.join(MOCK_DIR, 'kleinanzeigen_phone_0_1_6_3.json')
        with open(mock_file, 'r', encoding="utf-8") as file:
            mock_page_content = file.read()

        self.scraper = KleinanzeigenScraper(
            URL, page_content=mock_page_content)


    def test_get_phone_numbers(self):
        exp = ["01632485945"] # original -> 0 1 6 3 2 4 8 5 9 4 5
        act = self.scraper.get_seller_phones()
        self.assertEqual(exp, act, "Phone error")
