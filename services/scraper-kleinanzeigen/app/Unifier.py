
class Unifier:
    def __init__(self):
        self.mapping = {
            "PrivateSeller": "Private",

            # Ad status
            "Active": "ACTIVE",
            "OK": "ACTIVE",
            "Reserved": "RESERVED",
            "Inactive": "INACTIVE",
            "DELETED": "INACTIVE",
            "PAUSED" : "RESERVED",
            "Elektromotor": "Elektro",
            "PRO": "COMMERCIAL",
        }


        # 1) Tag mapping (source tag -> standardized tag)
        self.TAG_MAP = {
            "field_make_date": "firstRegistration",
            "field_kilometrage": "mileage",
            "field_engine": "engine",  # handled specially -> split into 2 rows
            "field_fuel_id": "fuel",
            "field_body_type_id": "bodyType",
            "field_number_of_doors_id": "doorCount",
            "field_wheel_drive_id": "drive",
            "field_gearbox_id": "transmission",
            "field_condition_type_id": "climatisation",
            "field_color_id": "color",
            "field_has_damaged_id": "damageCondition",
            "field_mot_date": "mot",
            "field_wheel_radius_id": "wheelSize",
            "field_weight": "kerbWeight",
            "field_number_of_seats_id": "numSeats",
            "field_id": "adId",
            "field_co2": "co2Emission",
        }

        # 2) Label mapping (standardized tag -> German label)
        self.LABEL_MAP_DE = {
            "firstRegistration": "Erstzulassung",
            "mileage": "Kilometerstand",
            "cubicCapacity": "Hubraum",
            "power": "Leistung",
            "fuel": "Kraftstoffart",
            "bodyType": "Fahrzeugtyp",
            "doorCount": "Anzahl der Türen",
            "drive": "Antriebsart",
            "transmission": "Getriebe",
            "climatisation": "Klimatisierung",
            "color": "Farbe",
            "damageCondition": "Fahrzeugzustand",
            "mot": "HU/AU gültig bis",
            "wheelSize": "Felgengröße",
            "kerbWeight": "Leergewicht (kg)",
            "numSeats": "Anzahl Sitzplätze",
            "adId": "Anzeige-ID",
            "co2Emission": "CO₂-Emission (g/km)",
        }

        # 3) Value normalization dictionary (raw -> German)
        self.VALUE_MAP = {
            # fuels
            "Petrol": "Benzin",
            "Diesel": "Diesel",
            "Hybrid": "Hybrid",
            "Electric": "Elektro",
            # transmission
            "Automatic": "Automatik",
            "Manual": "Schaltgetriebe",
            # drive
            "All wheel (4х4)": "Allrad (4x4)",
            "Front wheel": "Frontantrieb",
            "Rear wheel": "Heckantrieb",
            # climatisation
            "Climate control": "Klimaautomatik",
            "Air conditioning": "Klimaanlage",
            # damage/condition
            "No damages": "Unfallfrei",
            "Damaged": "Beschädigt",
            # colors (add more as needed)
            "Gray / silver": "Grau / Silber",
            "Black": "Schwarz",
            "White": "Weiß",
            "Blue": "Blau",
            "Red": "Rot",
            "Green": "Grün",
        }



        self.EQUIPMENT_MAP = {
            # Seats & Interior
            "Sport seats": "Sportsitze",
            "Leather seats": "Ledersitze",
            "Alcantara": "Alcantara",
            "Heated seats": "Sitzheizung",
            "Electric seats": "Elektr. Sitzeinstellung",
            "Electric seats with memory": "Elektr. Sitzeinstellung mit Memory-Funktion",
            "Multifunctional steering wheel": "Multifunktionslenkrad",
            "Paddle shifters": "Schaltwippen",
            "Voice commands": "Sprachsteuerung",
            "Dimming mirror": "Innenspiegel autom. abblendend",
            "Heated mirrors": "Beheizbare Außenspiegel",
            "Electric mirrors": "Elektr. Seitenspiegel",
            "Automatic folding mirrors": "Elektr. Seitenspiegel anklappbar",
            "Leather steering wheel": "Lederlenkrad",
            "Leather saloon": "Ledersalon",
            # Windows & Doors
            "Tinted windows": "Abgedunkelte Scheiben",
            "Electric boot lid": "Elektr. Heckklappe",
            "Keyless entry system": "Schlüssellose Zentralverriegelung (Keyless)",
            "Central locking": "Zentralverriegelung",
            # Lighting & Vision
            "Automatic headlamps": "Lichtsensor",
            "Rainfall sensor": "Regensensor",
            "Fog lights": "Nebelscheinwerfer",
            "LED headlights": "LED-Scheinwerfer",
            "LED daytime running lights": "LED-Tagfahrlicht",
            "Dynamic cornering lights": "Adaptives Kurvenlicht",
            "High beam assist": "Fernlichtassistent",
            "Headlights washers": "Scheinwerferreinigung",
            "Adaptive Cruise Control": "Abstandstempomat",
            "Collision prevention assist": "Notbremsassistent",
            "Blind Spot Detection": "Totwinkel-Assistent",
            "Lane Departure Warning": "Spurhalteassistent",
            "Road sign recognition": "Verkehrszeichenerkennung",
            "Rear view camera": "Rückfahrkamera",
            "Front view camera": "Frontkamera",
            "360° degree camera": "360° Kamera",
            # Comfort
            "Auxiliary heating": "Standheizung",
            "Cruise control": "Tempomat",
            "Start-Stop system": "Start/Stopp-Automatik",
            "Hill-start assist control": "Berganfahrassistent",
            "Head-Up display": "Head-Up Display",
            "Digital driver display": "Volldigitales Kombiinstrument",
            "LCD monitor": "Display",
            "Navigation/GPS": "Navigationssystem",
            "Handsfree kit": "Freisprecheinrichtung",
            "Apple CarPlay": "Apple CarPlay",
            "Android Auto": "Android Auto",
            "Apple CarPlay / Android Auto": "Apple CarPlay/Android Auto",
            "Climate control": "Klimanalage",
            # Audio
            "CD player": "CD-Spieler",
            "MP3 player": "MP3-Schnittstelle",
            "AUX input": "AUX-Eingang",
            "Subwoofer": "Subwoofer",
            "HiFi audio system": "Soundsystem",
            "USB input": "USB",
            # Security
            "Immobilizer": "Elektr. Wegfahrsperre",
            "Alarm": "Alarmanlage",
            "ESP": "ESP",
            "Traction control system": "Traktionskontrolle",
            # Exterior
            "Light alloy rims": "Leichtmetallfelgen",
            "Panoramic roof": "Panorama-Dach",
            "Sunroof": "Schiebedach",
            "Service book": "Scheckheftgepflegt",
            "Imported from US": "US-Import",
            "Set of winter tyres": "Winterreifen",
            "Spare wheel": "Reserverad",
            "Catalytic converter": "Katalysator",
            "Multiple key sets": "Mehrere Schlüssel",
        }


        self.BODY_TYPE = {
            "Wagon": "Kombi",
            "Saloon / sedan": "Limousine",
            "Hatchback" : "Limousine",
            "MPV / minivan": "Van Kleinbus",
            "Off-road / Crossover": "Geländewagen",
            "Coupe": "Sportwagen Coupe",
            "Commercial": "Van Kleinbus",
            "Convertible" : "Cabrio/Roadster",
            "Pick-up": "Geländewagen/Pickup/SUV",
            "Passenger minibus": "Van/Minibus",
            "Cargo van": "Van/Minibus",
            "Sedan": "Limousine",
            "SUV": "SUV",
            "Cabriolet": "Cabriolet",
        }

        self.VALUE_MAP.update(self.BODY_TYPE)  # Merge mapping into VALUE_MAP

        self.FUEL_TYPE = {
            "Electricity": "Elektro",
            "Petrol": "Benzin",
            "Gasoline": "Benzin",
        }

        self.SELLER_TYPE = {
            "Private": "Privat",
            "Dealer": "Händler",
        }

    def unify(self, value):
        unified_value = self.mapping.get(value)

        if unified_value is None:
            return value

        return unified_value

    def unify_tag(self, tag: str) -> str:
        unified_tag = self.TAG_MAP.get(tag, tag)

        if unified_tag is None:
            return tag

        return unified_tag

    def unify_label(self, tag: str) -> str:
        unified_label = self.LABEL_MAP_DE.get(tag, tag)

        if unified_label is None:
            return tag

        return unified_label

    def unify_value(self, value: str) -> str:
        # Handle unhashable types (e.g., list) gracefully
        try:
            unified_value = self.VALUE_MAP.get(value, value)
        except TypeError:
            # If value is unhashable (e.g., list), return as-is or join if list of strings
            if isinstance(value, list):
                # Optionally, join list items if all are strings
                if all(isinstance(v, str) for v in value):
                    return ', '.join(value)
                return str(value)
            return str(value)

        if unified_value is None:
            return value

        return unified_value

    def unify_technical_data(self, technical_data: list) -> list:
        # check if technical_data is emty
        if technical_data is None:
            return technical_data

        unified_technical_data = []

        for entry in technical_data:
            if not isinstance(entry, dict):
                unified_technical_data.append(entry)
                continue

            # Chec if entry has required fields
            if 'tag' not in entry or 'label' not in entry or 'value' not in entry:
                unified_technical_data.append(entry)
                continue

            unified_tag = self.unify_tag(entry['tag'])
            unified_label = self.unify_label(unified_tag)
            unified_value = self.unify_value(entry['value'])

        # Wite unified data. If initial, write original data
            unified_data = {
                "tag": unified_tag if unified_tag else entry['tag'],
                "label": unified_label if unified_label else entry['label'],
                "value": unified_value if unified_value else entry['value']
            }

            unified_technical_data.append(unified_data)

        return unified_technical_data

    def unify_equipment(self, equipment: list) -> list:
        if equipment is None:
            return []

        unified_equipment = []
        for eq in equipment:
            # If eq is not a string, skip it
            if not isinstance(eq, str):
                continue

            unified_value = self.EQUIPMENT_MAP.get(eq, eq)
            if unified_value is None:
                unified_equipment.append(eq)
            else:
                unified_equipment.append(unified_value)
        return unified_equipment

    def unify_body_type(self, body_type: str) -> str:
        unified_body_type = self.BODY_TYPE.get(body_type, body_type)

        if unified_body_type is None:
            return body_type

        return unified_body_type

    def unify_fuel_type(self, fuel_type: str) -> str:
        unified_fuel_type = self.FUEL_TYPE.get(fuel_type, fuel_type)

        if unified_fuel_type is None:
            return fuel_type

        return unified_fuel_type

    def standardize_phone_number(self, phone_number):
        if phone_number is None:
            return None

        phone_number = phone_number.replace(' ', '')

        if phone_number.startswith('0'):
            return phone_number

        if phone_number.startswith('+49(0)'):
            return phone_number.replace('+49(0)', '0')

        if phone_number.startswith('+4900'):
            return phone_number.replace('+4900', '0')

        if phone_number.startswith('+490'):
            return phone_number.replace('+490', '0')

        if phone_number.startswith('+49') and not phone_number.startswith('+490'):
            return phone_number.replace('+49', '0')

        if phone_number.startswith('+49'):
            return phone_number.replace('+49', '')
        # +370 686 54664


        return phone_number

    def remove_duplicate_phone_numbers(self, phone_numbers: list) -> list:
        if phone_numbers is None:
            return []

        result = []

        for number in phone_numbers:
            if number is None:
                continue

            if number == '':
                continue

            standardized_number = self.standardize_phone_number(number)

            if standardized_number not in result:
                result.append(standardized_number)

        return result

    def is_international_phone_number(self, phone_number: str) -> bool:
        # 37069037632
        if len(phone_number) == 11 and phone_number.startswith('37'):
            return True
        if phone_number.startswith('+3'):
            return True
        if phone_number.startswith('+4') and not phone_number.startswith('+49'):
            return True

    def unify_phone_number(self, phone_numbers: list) -> list:
        result = []

        unique_phone_numbers = self.remove_duplicate_phone_numbers(phone_numbers)

        for phone_number in unique_phone_numbers:
            if self.is_international_phone_number(phone_number):
                result.append(phone_number)
                continue

            result.append("+49" + phone_number)

        return result

    def unify_seller_type(self, seller_type) -> str:
        unified_seller_type = self.SELLER_TYPE.get(seller_type, seller_type)

        if unified_seller_type is None:
            return seller_type

        return unified_seller_type
