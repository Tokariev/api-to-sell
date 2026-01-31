from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class ParsedDataDto:
    url: str = None
    source: str = None
    externalCarId: str = None
    ad_status: str = None
    title: str = None
    brand: str = None
    model: str = None
    year: str = None
    first_registration: str = None
    body_type: str = None
    fuel_type: str = None
    model_variant: str = None
    description: str = None
    technical_data: list = field(default_factory=list)
    seller_phone: list = field(default_factory=list)
    contact_name: str = None
    contact_active_since: str = None
    equipment: list = field(default_factory=list)
    price: int = None
    price_rating: object = None
    price_history: list = field(default_factory=list)
    has_value_added_tax: bool = None
    is_negotiation_basis: bool = None
    seller_type: str = None
    postal_code: str = None
    city: str = None
    photo_urls: list = field(default_factory=list)
    has_full_service_history: bool = None
    has_car_accident: bool = None
    engine_power: list = field(default_factory=list)

    def to_dict(self):
        return asdict(self)
