SCRAPE_SUMMARY = "Scrape a Kleinanzeigen car listing"

SCRAPE_DESCRIPTION = (
    "Provide a Kleinanzeigen.de listing URL via the `url` query parameter. "
    "The URL must contain `kleinanzeigen.de/s-anzeige`. "
    "The response includes structured listing details (title, price, seller info, etc.) "
    "when available on the page."
)

SCRAPE_RESPONSE_EXAMPLE = {
    "url": "https://www.kleinanzeigen.de/s-anzeige/mazda-cx-5-2-2-diesel-automatik-leder-bose-ahk-gepflegt/3314195396-216-939",
    "source": "https://www.kleinanzeigen.de/s-anzeige/mazda-cx-5-2-2-diesel-automatik-leder-bose-ahk-gepflegt/3314195396-216-939",
    "externalCarId": "3314195396",
    "ad_status": "ACTIVE",
    "title": "Mazda CX-5 2.2 Diesel Automatik | Leder | Bose | AHK | gepflegt",
    "brand": "Mazda",
    "model": "CX Reihe",
    "year": "2016",
    "first_registration": "2016-05",
    "body_type": "SUV/Geländewagen",
    "fuel_type": "Diesel",
    "model_variant": "Method not implemented",
    "description": (
        "Zum Verkauf steht ein gepflegter Mazda CX-5 2.2 Turbodiesel mit Automatikgetriebe "
        "aus 2. Hand. Das Fahrzeug wurde von mir im Mai 2025 bei einem Händler gekauft und "
        "seitdem nur wenig gefahren. Der Verkauf erfolgt aus privaten Gründen. Die Kombination "
        "aus Crystal White Pearl Lack und weißer Lederausstattung wirkt sehr hochwertig und "
        "gepflegt – insbesondere bei Sonnenlicht kommt der Perleffekt des Lacks schön zur "
        "Geltung. Das Fahrzeug ist technisch einwandfrei, scheckheftgepflegt und ein "
        "Nichtraucherfahrzeug. Eine Händlergewährleistung aus dem Kauf im Mai 2025 besteht noch "
        "bis April 2026 (beim verkaufenden Autohaus). ZUSTAND Normale Gebrauchsspuren "
        "entsprechend Alter und Laufleistung. Kleine optische Macke an der hinteren Stoßstange "
        "(siehe Foto). Ansonsten ein sehr gepflegtes Fahrzeug mit sauberem Innenraum und einem "
        "insgesamt sehr guten Pflegezustand. AUSSTATTUNG (Auszug) - Weiße Lederausstattung "
        "(Vollleder) - Bose Soundsystem - Navigationssystem - LED-Scheinwerfer - Rückfahrkamera "
        "- Einparkhilfe vorne & hinten - Sitzheizung vorne - Elektrisch einstellbare Sitze "
        "(mit Memory-Funktion für den Fahrer) - Tempomat - Bluetooth & Freisprecheinrichtung "
        "- Anhängerkupplung (2.000 kg) - Spurhalteassistent - Blind Spot Monitoring "
        "(Toter-Winkel-Assistent) - Notbremsassistent - Automatisches Abschließen - "
        "Start-Stopp-System - Klimaanlage - Leichtmetallfelgen - Allwetterreifen Privatverkauf"
    ),
    "technical_data": [
        {"tag": "autos.marke", "label": "autos.marke", "value": "Mazda"},
        {"tag": "autos.model", "label": "autos.model", "value": "CX Reihe"},
        {"tag": "autos.km", "label": "autos.km", "value": "139.500 KM"},
        {"tag": "autos.schaden", "label": "autos.schaden", "value": "Unbeschädigtes Fahrzeug"},
        {"tag": "autos.ezdate", "label": "autos.ezdate", "value": "05/2016"},
        {"tag": "autos.fuel", "label": "autos.fuel", "value": "Diesel"},
        {"tag": "autos.power", "label": "autos.power", "value": "175 PS"},
        {"tag": "autos.shift", "label": "autos.shift", "value": "Automatik"},
        {"tag": "autos.typ", "label": "autos.typ", "value": "SUV/Geländewagen"},
        {"tag": "autos.anzahl_tueren", "label": "autos.anzahl_tueren", "value": "4/5 Türen"},
        {"tag": "autos.tuevdate", "label": "autos.tuevdate", "value": "Mai 2027"},
        {"tag": "autos.umweltplakette", "label": "autos.umweltplakette", "value": "4 (Grün)"},
        {"tag": "autos.aussenfarbe", "label": "autos.aussenfarbe", "value": "Weiß"},
        {
            "tag": "autos.material_innenausstattung",
            "label": "autos.material_innenausstattung",
            "value": "Vollleder",
        },
    ],
    "seller_phone": [],
    "contact_name": "L. Kröger",
    "contact_active_since": "06.02.17",
    "equipment": [
        "Anhängerkupplung",
        "Einparkhilfe",
        "Leichtmetallfelgen",
        "Xenon-/LED-Scheinwerfer",
        "Klimaanlage",
        "Navigationssystem",
        "Radio/Tuner",
        "Bluetooth",
        "Freisprecheinrichtung",
        "Sitzheizung",
        "Tempomat",
        "Nichtraucher-Fahrzeug",
        "Antiblockiersystem (ABS)",
        "Scheckheftgepflegt",
    ],
    "price": 15800,
    "price_rating": None,
    "price_history": [],
    "has_value_added_tax": None,
    "is_negotiation_basis": True,
    "seller_type": "Privat",
    "postal_code": "48153",
    "city": "Centrum",
    "photo_urls": [
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/5f/5f1748eb-a913-4890-a591-409b74d3091e?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/8f/8fc01cc8-d17c-4ef6-b82f-374f5248377b?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/da/daadb76b-0240-47c5-bb09-9ebd39ae9da2?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/3d/3dba0824-bd93-4870-bb2b-f93486225151?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/2f/2fff338b-1bae-4b04-a1e6-0de96f49134f?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/d6/d6aa928b-2701-43a4-b10a-dfdfeeb4bf1e?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/b6/b6618ea5-855b-4a6f-9a04-8cc551aa5f3f?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/16/1660d4b8-2c59-4faf-851a-d26063017d44?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/80/8024068b-d155-482f-930f-ba6c320d7031?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/45/454aa03e-2547-4345-9f00-2194856c8d59?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/00/00bb45ae-2ee1-4873-b1b3-920184cfc1e1?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/d8/d8ec58bb-0a61-4c56-b3dc-7fcec5bb0618?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/56/56aa945d-d75b-48a2-83da-9900fb43de47?rule=$_59.JPG",
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/50/5099f1ff-9ea4-4d06-b9de-c12446e4b48c?rule=$_59.JPG",
    ],
    "has_full_service_history": True,
    "has_car_accident": False,
    "engine_power": [],
}

SCRAPE_RESPONSES = {
    200: {
        "description": "Listing data extracted successfully.",
        "content": {"application/json": {"example": SCRAPE_RESPONSE_EXAMPLE}},
    },
    400: {"description": "Invalid URL. Must be a Kleinanzeigen.de listing URL."},
    502: {"description": "Upstream request failed while fetching the listing."},
}

SCRAPE_URL_DESCRIPTION = (
    "Full Kleinanzeigen.de listing URL. Must include the `/s-anzeige` path segment."
)

SCRAPE_URL_EXAMPLE = (
    "https://www.kleinanzeigen.de/s-anzeige/bmw-320d-2016/1234567890-216-1234"
)
