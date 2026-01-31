from datetime import datetime

from app.dto.ParsedDataDto import ParsedDataDto
from app.Unifier import Unifier


class Scraper(object):
    def __init__(self, url):
        self._url = url
        self.unifier = Unifier()

    def get_source(self):
        return self._url

    def get_external_car_id(self) -> str:
        return 'Method not implemented'

    def get_ad_status(self):
        return 'Method not implemented'

    def get_title(self):
        return 'Method not implemented'

    def get_brand(self):
        return 'Method not implemented'

    def get_model(self):
        return 'Method not implemented'

    def get_description(self) -> str:
        return 'Method not implemented'

    def get_technical_data(self):
        return []

    def get_seller_phones(self) -> list:
        return ['Method not implemented']

    def get_equipment(self):
        return 'Method not implemented'

    def get_price(self):
        return 'Method not implemented'

    def is_negotiation_basis(self):
        return 'Method not implemented'

    def get_seller_type(self):
        return 'Method not implemented'

    def get_postal_code(self):
        return 'Method not implemented'

    def get_city(self):
        return 'Method not implemented'

    def get_photo_urls(self) -> list:
        return 'Method not implemented'

    def has_full_service_history(self) -> bool:
        return 'Method not implemented'

    def has_value_added_tax(self) -> bool:
        return 'Method not implemented'

    def get_year(self):
        return 'Method not implemented'

    def get_first_registration(self) -> str:
        return 'Method not implemented'

    def get_body_type(self) -> str:
        return 'Method not implemented'

    def get_fuel_type(self):
        return 'Method not implemented'

    def get_model_variant(self):
        return 'Method not implemented'
    
    def get_publication_date(self):
        currentDateAndTime = datetime.now()

        return currentDateAndTime.strftime("%d.%m.%Y %H:%M:%S")
    
    def has_car_accident(self) -> bool:
        return 'Method not implemented'
    
    def get_contact_name(self) -> str:
        pass

    def get_contact_active_since(self) -> str:
        pass


    def fetch_data(self) -> ParsedDataDto:
        data = ParsedDataDto(
            url = self._url,
            source = self.get_source(),
            externalCarId = self.get_external_car_id(),
            ad_status = self.get_ad_status(),
            title = self.get_title(),
            brand = self.get_brand(),
            
            model = self.get_model(),
            year = self.get_year(),
            first_registration = self.get_first_registration(), # 2020-01
            body_type = self.unifier.unify_body_type(self.get_body_type()),   # Kombi
            fuel_type = self.unifier.unify_fuel_type(self.get_fuel_type()),   # Benzin  / Diesel
            model_variant = self.get_model_variant(),                         # 1.6 TDI 110 kW
            
            description = self.get_description(),
            technical_data = self.unifier.unify_technical_data(self.get_technical_data()) ,
            seller_phone = self.unifier.unify_phone_number( self.get_seller_phones() ),
            contact_name = self.get_contact_name(),
            contact_active_since  = self.get_contact_active_since(),

            equipment = self.unifier.unify_equipment(self.get_equipment()),
            price = self.get_price(),
            has_value_added_tax = self.has_value_added_tax(),
            is_negotiation_basis = self.is_negotiation_basis(),
            seller_type = self.unifier.unify_seller_type( self.get_seller_type() ),
            
            postal_code = self.get_postal_code(),
            city = self.get_city(),
            photo_urls = self.get_photo_urls(),
            has_full_service_history = self.has_full_service_history(),
            has_car_accident = self.has_car_accident(),
            engine_power= [],
        )

        # data.engine_power = self.fetch_engine_power(data)
        
        return data
