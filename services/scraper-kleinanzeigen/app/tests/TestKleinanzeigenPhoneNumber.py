import unittest
import os
from app.KleinanzeigenScraper import KleinanzeigenScraper

URL = "https://www.kleinanzeigen.de/s-anzeige/vw-sharan-1-4-tsi-dsg-comforline-2023-unfall-autos/3009408190-216-794"
MOCK_DIR = os.path.join(os.path.dirname(__file__), '..', 'mock')


class TestKleinanzeigenPhoneNumber(unittest.TestCase):
    def test_get_phone_numbers(self):
        mock_file = os.path.join(MOCK_DIR, 'kleinanzeigen_dont_recognize_phone_numb.json')
        with open(mock_file, 'r', encoding="utf-8") as file:
            mock_page_content = file.read()

        self.scraper = KleinanzeigenScraper(
            URL, page_content=mock_page_content)

        exp = ['015255272775']
        act = self.scraper.get_seller_phones()
        self.assertEqual(exp, act)

    def test_get_phone_numbers_2(self):
        mock_file = os.path.join(MOCK_DIR, 'kleinanzeigen_phone_was_not_recognized.json')
        with open(mock_file, 'r', encoding="utf-8") as file:
            mock_page_content = file.read()

        self.scraper = KleinanzeigenScraper(
            URL, page_content=mock_page_content)

        exp = ['+4915737330728']
        act = self.scraper.get_seller_phones()
        self.assertEqual(exp, act)
