SCRAPE_SUMMARY = "Kleinanzeigen.de car scraper"

SCRAPE_DESCRIPTION = (
    "Provide a Kleinanzeigen.de listing URL via the `url` query parameter. "
    "The URL must contain `kleinanzeigen.de/s-anzeige`. "
    "The response includes structured listing details (title, price, seller info, etc.) "
    "when available on the page."
)

SCRAPE_RESPONSES = {
    200: {"description": "Listing data extracted successfully."},
    400: {"description": "Invalid URL. Must be a Kleinanzeigen.de listing URL."},
    502: {"description": "Upstream request failed while fetching the listing."},
}

SCRAPE_URL_DESCRIPTION = (
    "Full Kleinanzeigen.de listing URL. Must include the `/s-anzeige` path segment."
)

SCRAPE_URL_EXAMPLE = (
    "https://www.kleinanzeigen.de/s-anzeige/bmw-320d-2016/1234567890-216-1234"
)
