import unittest

from app.DemoCar import DemoCar
from app.main import scrape

DEMO_URL = "https://www.kleinanzeigen.de/s-anzeige/demo-car/123456789-123-12345"


class TestDemoCar(unittest.TestCase):

    def test_matches_demo_url(self):
        self.assertTrue(DemoCar.matches(DEMO_URL))

    def test_does_not_match_real_listing(self):
        url = "https://www.kleinanzeigen.de/s-anzeige/mazda-cx-5/3478846203-216-30266"
        self.assertFalse(DemoCar.matches(url))

    def test_scrape_returns_demo_payload(self):
        result = scrape(url=DEMO_URL)

        self.assertEqual('Mazda', result.brand)
        self.assertEqual('CX Reihe', result.model)
        self.assertEqual(15800, result.price)
        self.assertEqual('ACTIVE', result.ad_status)
        self.assertEqual(['+491785577550'], result.seller_phone)
        self.assertEqual(9, len(result.technical_data))
        self.assertEqual(4, len(result.photo_urls))
