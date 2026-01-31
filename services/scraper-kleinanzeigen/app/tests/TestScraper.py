import unittest
from app.dto.ParsedDataDto import ParsedDataDto
from app.Scraper import Scraper


class TestScraper(unittest.TestCase):
    def test_fetch_data(self):
        URL = "https://www.ebay-kleinanzeigen.de/s-anzeige/2324472366"

        cut = Scraper(URL)
        act = cut.fetch_data()

        self.assertIsInstance(act, ParsedDataDto)
