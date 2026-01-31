from app.KleinanzeigenScraper import KleinanzeigenScraper
from app.ScraperError import ScraperError

class ScraperFactory(object):

    @staticmethod
    def create_scraper(url: str):
        if "kleinanzeigen.de/s-anzeige" in url:
            return KleinanzeigenScraper(url, check_duplicate=False)

        raise ScraperError(f"Unsupported URL: {url}")
