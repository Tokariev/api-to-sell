import unittest
import os
from app.KleinanzeigenScraper import KleinanzeigenScraper

URL = "https://www.ebay-kleinanzeigen.de/s-anzeige/2324472366"
MOCK_DIR = os.path.join(os.path.dirname(__file__), '..', 'mock')


class TestKleinanzeigenContactName(unittest.TestCase):
    def setUp(self):
        mock_file = os.path.join(MOCK_DIR, 'kleinanzeige_contact_name.json')
        with open(mock_file, 'r', encoding="utf-8") as file:
            mock_page_content = file.read()

        self.scraper = KleinanzeigenScraper(
            URL, page_content=mock_page_content)


    def test_get_contact_name(self):
        exp = "Schorsch"
        act = self.scraper.get_contact_name()
        self.assertEqual(exp, act, "Contact name is wrong")

    def test_get_contact_active_since(self):
        # exp = "2015-09-08"
        exp = "08.09.15"
        act = self.scraper.get_contact_active_since()
        self.assertEqual(exp, act, "Contact active since is wrong")
