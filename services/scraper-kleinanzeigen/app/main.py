import os
import re

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

from app.KleinanzeigenScraper import KleinanzeigenScraper
from app.RequestError import RequestError
from app.docs import (
    SCRAPE_DESCRIPTION,
    SCRAPE_RESPONSES,
    SCRAPE_SUMMARY,
    SCRAPE_URL_DESCRIPTION,
    SCRAPE_URL_EXAMPLE,
)

app = FastAPI(
    title="Kleinanzeigen Scraper API",
    description="Scrapes car listing data from Kleinanzeigen.de",
    version="1.0.0",
    root_path=os.getenv("ROOT_PATH", ""),
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get(
    "/api/scrape",
    summary=SCRAPE_SUMMARY,
    description=SCRAPE_DESCRIPTION,
    responses=SCRAPE_RESPONSES,
)
def scrape(
    url: str = Query(
        ...,  # required
        description=SCRAPE_URL_DESCRIPTION,
        example=SCRAPE_URL_EXAMPLE,
    )
):
    if "kleinanzeigen.de/s-anzeige" not in url:
        raise HTTPException(status_code=400, detail="URL must be a kleinanzeigen.de listing URL")

    try:
        scraper = KleinanzeigenScraper(url, check_duplicate=False)
        data = scraper.fetch_data()
        return JSONResponse(content=data.to_dict())
    except RequestError as e:
        raise HTTPException(status_code=502, detail=str(e))
