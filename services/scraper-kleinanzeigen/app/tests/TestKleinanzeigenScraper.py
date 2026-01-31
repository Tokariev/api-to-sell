import unittest
import os
from app.KleinanzeigenScraper import KleinanzeigenScraper

URL = "https://www.ebay-kleinanzeigen.de/s-anzeige/2324472366"
MOCK_DIR = os.path.join(os.path.dirname(__file__), '..', 'mock')


class TestMobileSvcScraper(unittest.TestCase):
    def setUp(self):
        mock_file = os.path.join(MOCK_DIR, 'kleinanzeigen_bmw_x5.json')
        with open(mock_file, 'r', encoding="utf-8") as file:
            mock_page_content = file.read()

        self.scraper = KleinanzeigenScraper(
            URL, page_content=mock_page_content)

    def test_get_external_car_id(self):
        exp = "2324472366"
        act = self.scraper.get_external_car_id()
        self.assertEqual(exp, act, "External car ID not found")
    
    def test_create_url(self):
        url = "https://www.ebay-kleinanzeigen.de/s-anzeige/2324472366"
        exp = "https://api.kleinanzeigen.de/api/ads/2324472366.json"
        act = self.scraper.create_api_url(URL)
        self.assertEqual( exp, act, "URL not created correctly")
        
        url = "https://www.ebay-kleinanzeigen.de/s-anzeige/118i-bmw-136-ps/2355112235-216-18675"
        exp = "https://api.kleinanzeigen.de/api/ads/2355112235.json"
        act = self.scraper.create_api_url(url)
        self.assertEqual(exp, act, "URL not created correctly")

    def test_get_brand(self):
        exp = self.scraper.get_brand()
        self.assertEqual(exp, "BMW", "Brand not found")

    def test_get_model(self):
        exp = "X5 3.0SD Tüv 2024"
        act = self.scraper.get_model()
        self.assertEqual(exp, "X5 3.0SD Tüv 2024", "Model not correct") #"Bmw X5 3.0SD Tüv 2024", "Model not found"

    # Only for kleinanzeigen relevant
    def test_get_phone_numbers(self):
        exp = ['+4917660466226']
        text = "In diesem Inserat wird ein Bmw X5 3.0SD Motor mit 330PS veräußert. Das Fahrzeug befindet sich in einem recht soliden Zustand sowohl Motor als auch Getriebe laufen einwandfrei. Optisch hat der Wagen keinerlei Gebrauchtspuren da ich das auto recht gepflegt halte. TÜV hat er noch bis zum November 2024. Ich besitze das auto seid circa 2 Jahren und muss sagen das es mich bis jetzt noch nie im stich gelassen hat. Nun nochmal eine Zusammenfassung der Sonderausstattung:<br />-Radio audio<br />-Bluetooth<br />-Freisprecheinrichtung<br />-Aux Anschluss<br />-Zweizonen Klimaautomatik<br />-Sitzheizung<br />-Elektrisch verstellbare Außenspiegel<br />-Elektrisch verstellbare Sitze<br />-Lederlenkrad<br />-BiXenon&#x2F;Xenon<br />-Metallic Lackierung<br />etc.<br /><br /><br />Mängel: Panoramadach lässt sich nicht mehr schließen Elektronik funktioniert aber eine Seite schließt die andere ist am hängen muss etwas kleines gemacht werden. Und Kardanwellen gummi muss gewechselt werden im niedrigere Drehzahl stottert der bißchen wenn man dann gas gibt ist alles normal beeinträchtigt nicht die Fahrweise.<br /><br /><br />Falls irgendwelche Fragen offen bleiben könnt ihr euch gerne telefonisch bei mir melden oder mich per Nachricht Kontaktieren.<br /><br />Tell: +49 176 60466226"
        self.assertEqual(exp, self.scraper.get_phone_numbers_by_regex(
            text), "Phone number not found")

    # Only for kleinanzeigen relevant
    def test_get_phone_numbers_multiple(self):
        exp = ['+4917660466226',
               '+4917660466227',
               '017660466228',
               ]
        text = "In diesem Inserat wird ein Bmw X5 3.0SD Motor mit 330PS veräußert. Das Fahrzeug befindet sich in einem recht soliden Zustand sowohl Motor als auch Getriebe laufen einwandfrei. Optisch hat der Wagen keinerlei Gebrauchtspuren da ich das auto recht gepflegt halte. TÜV hat er noch bis zum November 2024. Ich besitze das auto seid circa 2 Jahren und muss sagen das es mich bis jetzt noch nie im stich gelassen hat. Nun nochmal eine Zusammenfassung der Sonderausstattung:<br />-Radio audio<br />-Bluetooth<br />-Freisprecheinrichtung<br />-Aux Anschluss<br />-Zweizonen Klimaautomatik<br />-Sitzheizung<br />-Elektrisch verstellbare Außenspiegel<br />-Elektrisch verstellbare Sitze<br />-Lederlenkrad<br />-BiXenon&#x2F;Xenon<br />-Metallic Lackierung<br />etc.<br /><br /><br />Mängel: Panoramadach lässt sich nicht mehr schließen Elektronik funktioniert aber eine Seite schließt die andere ist am hängen muss etwas kleines gemacht werden. Und Kardanwellen gummi muss gewechselt werden im niedrigere Drehzahl stottert der bißchen wenn man dann gas gibt ist alles normal beeinträchtigt nicht die Fahrweise.<br /><br /><br />Falls irgendwelche Fragen offen bleiben könnt ihr euch gerne telefonisch bei mir melden oder mich per Nachricht Kontaktieren.<br /><br />Tell: +49 176 60466226 oder +4917660466227 oder 017660466228"
        self.assertEqual(exp, self.scraper.get_phone_numbers_by_regex(
            text), "Multiple phone numbers")

    def test_get_seller_phones(self):
        exp = ['+4917660466226']
        act = self.scraper.get_seller_phones()
        self.assertEqual(exp, act, "Seller phone number not found")

    def test_get_description(self):
        exp = "In diesem Inserat wird ein Bmw X5 3.0SD Motor mit 330PS veräußert. Das Fahrzeug befindet sich in einem recht soliden Zustand sowohl Motor als auch Getriebe laufen einwandfrei. Optisch hat der Wagen keinerlei Gebrauchtspuren da ich das auto recht gepflegt halte. TÜV hat er noch bis zum November 2024. Ich besitze das auto seid circa 2 Jahren und muss sagen das es mich bis jetzt noch nie im stich gelassen hat. Nun nochmal eine Zusammenfassung der Sonderausstattung: -Radio audio -Bluetooth -Freisprecheinrichtung -Aux Anschluss -Zweizonen Klimaautomatik -Sitzheizung -Elektrisch verstellbare Außenspiegel -Elektrisch verstellbare Sitze -Lederlenkrad -BiXenon/Xenon -Metallic Lackierung etc. Mängel: Panoramadach lässt sich nicht mehr schließen Elektronik funktioniert aber eine Seite schließt die andere ist am hängen muss etwas kleines gemacht werden. Und Kardanwellen gummi muss gewechselt werden im niedrigere Drehzahl stottert der bißchen wenn man dann gas gibt ist alles normal beeinträchtigt nicht die Fahrweise. Falls irgendwelche Fragen offen bleiben könnt ihr euch gerne telefonisch bei mir melden oder mich per Nachricht Kontaktieren. Tell: +49 176 60466226"
        act = self.scraper.get_description()
        self.assertEqual(exp, act, "Description not found")

    def test_technical_data(self):
        exp = [
            {
                "tag": "autos.marke",
                "label": "Marke",
                "value": "BMW"
            },
            {

                "tag": "autos.model",
                "label": "Modell",
                "value": "X Reihe"
            },
            {

                "tag": "autos.km",
                "label": "Kilometerstand",
                "value": "317.000 KM"
            },
            {

                "tag": "autos.schaden",
                "label": "Fahrzeugzustand",
                "value": "Unbeschädigtes Fahrzeug"
            },
            {

                "tag": "autos.ezdate",
                "label": "Erstzulassung",
                "value": "11/2008"
            },
            {

                "tag": "autos.fuel",
                "label": "Kraftstoffart",
                "value": "Diesel"
            },
            {

                "tag": "autos.power",
                "label": "Leistung",
                "value": "330 PS"
            },
            {

                "tag": "autos.shift",
                "label": "Getriebe",
                "value": "Automatik"
            },
            {

                "tag": "autos.typ",
                "label": "Fahrzeugtyp",
                "value": "SUV/Geländewagen"
            },
            {

                "tag": "autos.anzahl_tueren",
                "label": "Anzahl Türen",
                "value": "4/5 Türen"
            },
            {

                "tag": "autos.tuevdate",
                "label": "HU bis",
                "value": "November 2024"
            },
            {

                "tag": "autos.umweltplakette",
                "label": "Umweltplakette",
                "value": "4 (Grün)"
            },
            {

                "tag": "autos.schadstoffklasse",
                "label": "Schadstoffklasse",
                "value": "Euro4"
            },
            {

                "tag": "autos.aussenfarbe",
                "label": "Außenfarbe",
                "value": "Silber"
            },
            {

                "tag": "autos.material_innenausstattung",
                "label": "Material Innenausstattung",
                "value": "Vollleder"
            }
        ]
        act = self.scraper.get_technical_data()
        self.assertEqual(exp, act, "Technical data not found")

    def test_get_equipment(self):
        exp = [
                "Einparkhilfe",
                "Leichtmetallfelgen",
                "Xenon-/LED-Scheinwerfer",
                "Klimaanlage",
                "Navigationssystem",
                "Radio/Tuner",
                "Bluetooth",
                "Freisprecheinrichtung",
                "Schiebedach/Panoramadach",
                "Sitzheizung",
                "Tempomat",
                "Nichtraucher-Fahrzeug",
                "Antiblockiersystem (ABS)",
            ]
        act = self.scraper.get_equipment()
        self.assertEqual(exp, act, "Equipment is wrong")
        

    def test_seller_type(self):
        exp = "Privat"
        act = self.scraper.get_seller_type()
        self.assertEqual(exp, act, "Seller type is wrong")

    def test_get_postal_code(self):
        exp = '46047'
        act = self.scraper.get_postal_code()
        self.assertEqual(exp, act, "Postal code not found")

    def test_get_city(self):
        exp = 'Oberhausen'
        act = self.scraper.get_city()
        self.assertEqual(exp, act, "City not found")

    def test_get_photo_urls(self):
        exp = [
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/07/078af5cd-cf66-4bff-bdc4-de064d6234f1?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/c7/c76c0bfc-51b3-4c2c-914d-7727ee7a0471?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/40/4084f02a-12ea-4427-bdcf-436330cad596?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/b3/b3e8918a-3215-4419-b90c-bd1a41945972?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/60/60e2d9d8-74a2-4b27-8da6-ccff2f21089e?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/a3/a3e329c6-07b4-4a23-a5ef-631bdd3bc993?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/1a/1a742b4d-d99d-4391-b911-c7d47274ecc4?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/15/15333717-88e1-4d37-9c4d-f7ab5e378b95?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/81/81834db6-dff3-4075-82a9-18a9fa029f4f?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/21/212cf19f-7fbf-4f9d-8a22-95f520332c60?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/25/257a891a-a8e4-4e4a-880b-c3e8b67c8faf?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/b3/b327d5a2-dd7b-415b-9063-67a8ab517322?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/a7/a769c093-0046-496c-8771-5a6180ec8883?rule=$_59.JPG",
            "https://img.ebay-kleinanzeigen.de/api/v1/prod-ads/images/39/394c0032-016c-492a-aab4-e6df76cf12b8?rule=$_59.JPG",
        ]
        act = self.scraper.get_photo_urls()
        self.assertEqual(exp, act, "Photo urls not found")

    def test_is_negotiation_basis(self):
        exp = True
        act = self.scraper.is_negotiation_basis()
        self.assertEqual(exp, act, "Ptice type is wrong")

    def test_get_price(self):
        exp = 9800.00
        act = self.scraper.get_price()
        self.assertEqual(exp, act, "Ptice is wrong")
    
    def test_get_year(self):
        exp = "2008"
        act = self.scraper.get_year()
        self.assertEqual(exp, act, "Year is wrong")
    
    def test_get_first_registration(self):
        exp = "2008-11"
        act = self.scraper.get_first_registration()
        self.assertEqual(exp, act, "First registration date is wrong")

    def test_phone_number_at_beginn(self):
        mock_file = os.path.join(MOCK_DIR, 'kleinanzeige_phone_at_beginn.json')
        with open(mock_file, 'r', encoding="utf-8") as file:
            mock_page_content = file.read()

        self.scraper = KleinanzeigenScraper(
            URL, page_content=mock_page_content)
        
        exp = ['01638560563']
        act = self.scraper.get_seller_phones()
        self.assertEqual(exp, act, "Seller phone number not found")