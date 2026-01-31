import unittest
import os
from app.KleinanzeigenScraper import KleinanzeigenScraper

URL = "https://www.ebay-kleinanzeigen.de/s-anzeige/2324472366"
MOCK_DIR = os.path.join(os.path.dirname(__file__), '..', 'mock')


class TestKleinanzeigenWeitereAutomarken(unittest.TestCase):
    def setUp(self):
        mock_file = os.path.join(MOCK_DIR, 'kleinanzeigen_weitere_automarken.json')
        with open(mock_file, 'r', encoding="utf-8") as file:
            mock_page_content = file.read()

        self.scraper = KleinanzeigenScraper(
            URL, page_content=mock_page_content)

    
    def test_get_model(self):
        # exp = "Auto Mercedes c200 w204 AMG Line Packet evt Tausch"
        exp = "Weitere Automarken"
        act = self.scraper.get_model() 
        self.assertEqual(exp, act, "Automarke is not correct")
    