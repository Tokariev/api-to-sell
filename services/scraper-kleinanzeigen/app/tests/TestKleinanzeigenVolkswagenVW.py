import unittest
import os
from app.KleinanzeigenScraper import KleinanzeigenScraper

URL = "https://www.ebay-kleinanzeigen.de/s-anzeige/2324472366"
MOCK_DIR = os.path.join(os.path.dirname(__file__), '..', 'mock')


class TestMobileSvcScraper(unittest.TestCase):
    def setUp(self):
        mock_file = os.path.join(MOCK_DIR, 'kleinanzeigen_volkswagen_vw.json')
        with open(mock_file, 'r', encoding="utf-8") as file:
            mock_page_content = file.read()

        self.scraper = KleinanzeigenScraper(
            URL, page_content=mock_page_content)


    def test_brand(self):
        exp = 'Volkswagen'
        act = self.scraper.get_brand()
        self.assertEqual(exp, act)

    def test_model(self):
        # exp = 'Golf 7, 8-f.Bereif,TÜV; Klima, Automatik,Scheckheft, Wie Neu!'
        exp = 'Golf'
        act = self.scraper.get_model()
        self.assertEqual(exp, act, "Model error")
