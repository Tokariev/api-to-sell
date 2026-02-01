from typing import Any, List, Optional

from pydantic import BaseModel


class TechnicalDataItemDto(BaseModel):
    tag: Optional[str] = None
    label: Optional[str] = None
    value: Optional[str] = None


class ParsedDataResponseDto(BaseModel):
    url: Optional[str] = None
    source: Optional[str] = None
    externalCarId: Optional[str] = None
    ad_status: Optional[str] = None
    title: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[str] = None
    first_registration: Optional[str] = None
    body_type: Optional[str] = None
    fuel_type: Optional[str] = None
    model_variant: Optional[str] = None
    description: Optional[str] = None
    technical_data: List[TechnicalDataItemDto] = []
    seller_phone: List[str] = []
    contact_name: Optional[str] = None
    contact_active_since: Optional[str] = None
    equipment: List[str] = []
    price: Optional[float] = None
    has_value_added_tax: Optional[bool] = None
    is_negotiation_basis: Optional[bool] = None
    seller_type: Optional[str] = None
    postal_code: Optional[str] = None
    city: Optional[str] = None
    photo_urls: List[str] = []
    has_full_service_history: Optional[bool] = None
    has_car_accident: Optional[bool] = None