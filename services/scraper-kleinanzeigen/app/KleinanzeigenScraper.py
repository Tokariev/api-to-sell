import re
import json
import html
import requests
from app.Unifier import Unifier
from translate.Translater import Translater
from app.Scraper import Scraper
from app.RequestError import RequestError
from utils.HtmlCharacterDecoder import HtmlCharacterDecoder
from app.NestedValue import get_nested_value
from app.ExternalCarID import ExternalCarID


class KleinanzeigenScraper(Scraper):
    
    def __init__(self, url, check_duplicate=True, enable_proxy=False, page_content=None):
        super().__init__(url)

        self.check_strsategy = None

        ### Mocking
        if page_content is not None:
            page_content_json = json.loads(page_content)
            self.value = page_content_json["{http://www.ebayclassifiedsgroup.com/schema/ad/v1}ad"]["value"]
            return
        ### End of mocking

        API_URL = self.create_api_url(url)

        payload = {}
        headers = {
            'Host': 'api.kleinanzeigen.de',
            'Cookie': 'ak_bmsc=668ED90B79A1F8154A7CDF2A6ECC9E44~000000000000000000000000000000~YAAQa1ITAjB8QNyLAQAA1GLdDBXl+tztBb8Ej/GEsAMvGkzU0WdvvHi/hFzTwaKplFiflbgvrNVBby9NcCEv3tqoVSdU40sSszIQJv2Zn7MmVVGy6NGsVwg78JlCgyR//pit2vbewDtzwf10n7ShBv1q5zLfrG9MuyG6U/DmOzBal86dOWrszNLnOO/9i8O7zjkhztcwOg59rsisR+9W3mJZnJDsqUDK92e3c9MQC7c28jnlPLL61Cmh0CbMEkZF4KMRy+A55f7OreaMefI4YUcOSpdHCvwaA2xRLZXKAKcsif9InUdCqwpICrmzOHbShUf55QweYNh1Ry3Afm5VNEeHT2giadG/vLd7y143m3N/PAjmp0D5gMBdlXlAr1QX3c1eh9zEmszGTd5oEeoS2I4=',
            'x-ebayk-usecase': 'vip',
            'x-ecg-in': 'ad-address,ad-external-reference-id,ad-guid,ad-source-id,ad-status,ad-type,attributes,buy-now,category,contact-name,contact-name-initials,description,displayoptions,documents,features-active,id,imprint,link,locations.location.id,locations.location.regions.region.localized-name,medias,otherAttributes,partnership,phone,pictures,poster-type,price,search-distance,seller-account-type,shipping-options,start-date-time,store-id,title,user-id,user-rating,user-since-date-time,userBadges',
            'accept': '*/*',
            'authorization': 'Basic aXBob25lOmc0Wmk5cTEw',
            'x-ecg-ver': '1.16',
            'accept-language': 'de-DE;q=1.0, en-DE;q=0.9, ru-DE;q=0.8',
            'user-agent': 'Kleinanzeigen/15.13.0 (com.ebaykleinanzeigen.ebc; build:145712; iOS 17.1.1) Alamofire/5.8.0',
            'x-ecg-user-agent': 'ebayk-iphone-app-145712',
            'x-ebayk-app': '3501901B-2A9B-4883-B9C8-C726D093930F',
            'x-ebayk-groups': 'BIPHONE-5507_algolia_ux_R|BIPHONE-6269_POST_AD_DIA_A|BIPHONE-6518_ATT_12_11_1_R|BIPHONE-6518_ATT_12_12_0_C|BIPHONE-6518_ATT_D|BIPHONE-7261_KYC_triggers_D|BIPHONE-7483_ComFlag_A|BIPHONE-7595_ga_behind_B|BIPHONE-7678_oauth_B|BIPHONE-7710_SHIP_POST_AD_B|BIPHONE-8000_BuyNow_Final_A|BIPHONE-8202_offer_make_B|BIPHONE-8577_post_ph_kill_B|BIPHONE-8771_buyer_banner_A|BIPHONE-8797_Akamai_kill2_B|BIPHONE-9002_SRPSuggests_A|BIPHONE-9062_Loc_Sel_Kit_B|BIPHONE-9089_promo_kill_A|BIPHONE-9167_Categories_A|BIPHONE-9179_category_rec_B|BIPHONE-9187_StarToHeart_A|BIPHONE-9291_MyAdsC2b_C|BIPHONE-9420_re_post_A|BIPHONE-9624-Transaction_B|BIPHONE-9686_Location_Sel_A|BIPHONE-9700_buy_now_B|BIPHONE-9730_Pushes_A|BIPHONE-9756-nudge-buyer_A|BIPHONE-9763_intersitial_B|BIPHONE-9773-Bottom-Navi_A|BIPHONE-9778-remove-VB-op_A|BIPHONE-9827_Promote_BuyN_A|BIPHONE-9885_sust_tag_B|BIPHONE5592_tmx_login_A|BIPHONE5709_ENRICHSRP_v2_A|BIPHONE5772_Conversations_R|BIPHONE7754-make_offer_B|BIPHONE7792_SellerRefund2_A|BIPHONE7799_Seller_Refund_B|BIPHONE8444-BuyNowCheckou_B|BIPHONE8816_OfferReminder_B|BIPHONE8900_recomShipping_D|BIPHONE9002_SRPSuggestion_A|BIPHONE9070-srp_pic_count_B|BIPHONE9686_Loc_Selection_B|BIPHONE9898_BanCategory_A|BIPHONE_postAd_FlipBuyNow_C|EBAYK1592_PostAd_Category_B|EKA-6183_White_Header_v2_B|EKA-6636_borders_ios_B|EKA-6698_font_ios_B|EKA_6376_Rebr_Master_ios_B|FeedbackCenter_A|SettingsPage2_B|filter_ux_part1_B|iOS_FeedExperimentsPTwo_B|iOS_FeedExperiments_C|iOS_FeedSurvey_B|iOS_NewFeedSections_C|iOS_Payment_SRP_B|iOS_PromoArticleSep23_A|liberty_gcp_ios_B|relper_icas_soft_filter_E|typo_ios_A'
        }
                        

        # Real data
        try:
            requests.packages.urllib3.disable_warnings()
            res = requests.request(
                "GET", API_URL, headers=headers, data=payload, verify=False, timeout=10, )
        except requests.exceptions.Timeout as err:
            raise RequestError('Kleinanzeige timeout:', err)
        except requests.exceptions.ConnectionError as err:
            raise RequestError('Kleinanzeige connection error:', err)    
        except requests.exceptions.HTTPError as err:
            raise RequestError('Kleinanzeige bad respone:', err)

        # Not found, ad was deleted
        if res.status_code == 404:
            print(res.status_code)
            self.value = {}
            return

        try:
            res_json = res.json()
            # Write response to file
            # with open('kleinanzeigen_same_car_as_on_autoscout24.json', 'w') as f:
            #     f.write(json.dumps(res_json, indent=4))
        except:
            raise RequestError('Kleinanzeige bad json.\n' + str(res.text))

        try:
            ad_value = res_json["{http://www.ebayclassifiedsgroup.com/schema/ad/v1}ad"]["value"]
        except KeyError:
            raise RequestError('Kleinanzeige bad json.')
        

        self.value = ad_value

    def get_external_car_id(self):
        return ExternalCarID().extract_id_by_url(self._url)

    def create_api_url(self, origianl_link):
        ad_id = ExternalCarID().extract_id_by_url(origianl_link)
        return "https://api.kleinanzeigen.de/api/ads/" + ad_id + ".json"

    def get_ad_status(self):
        if self.value == {}:
            return 'INACTIVE'

        ad_status = get_nested_value(self.value, ["ad-status", "value"])
        
        return Unifier().unify(ad_status)

    def get_price(self): 
        price = get_nested_value(self.value, ["price", "amount", "value"])
        if price is None:
            return None
        
        # Check if price is a float number
        try:
            float(price)
            price = int(float(price))
        except ValueError:
            pass

        return price
        

    def has_value_added_tax(self) -> bool:
        title = self.get_title()

        if title is None:
            return None
        
        if "mwst" in title.lower():
            return True

        description = self.get_description()
        if "mwst" in description.lower():
            return True

    def is_negotiation_basis(self):
        price_type = get_nested_value(self.value, ["price", "price-type", "value"])

        if price_type == 'PLEASE_CONTACT':
            return True
        else:
            return False


    def get_brand(self):
        brand = get_nested_value(self.value, ["attributes", "attribute", 0, "value", 0, "localized-label"])

        if brand == "Weitere Automarken":
            return ""
        
        return brand

    def get_title(self):
        title = get_nested_value(self.value, ["title", "value"])
        return HtmlCharacterDecoder().escape_html_codes(title)

    def get_model(self):
        # Title from kleinanzeigen.de => VW Golf 7, 8-f.Bereif,TÜV neu, 1.Hand, 1.9TDI, 105PS, 5-Gang
        # title = self.get_title()
        # brand = self.get_brand()
        
        # Golf 7, 8-f.Bereif,TÜV; Klima, Automatik,Scheckheft, Wie Neu! 
        # return KleinanzeigenModel(brand, title).get_model()

        attribute_list = get_nested_value(self.value, ["attributes", "attribute"])
        
        if attribute_list is None:
            return None  

        for item in attribute_list:
            if item["name"] == "autos.model":
                return item["value"][0]["localized-label"]
                
        return 'Weitere Automarken'


    def get_body_type(self):
        attributes = get_nested_value(self.value, ["attributes", "attribute"])    

        if attributes is None:
            return None

        for item in attributes:
            if item["name"] == "autos.typ":
                return item["value"][0]["localized-label"]

    def get_fuel_type(self):
        attributes = get_nested_value(self.value, ["attributes", "attribute"])

        if attributes is None:
            return None
        
        for item in attributes:
            if item["name"] == "autos.fuel":
                return item["value"][0]["localized-label"]

    def get_year(self):
        attributes = get_nested_value(self.value, ["attributes", "attribute"])
        
        if attributes is None:
            return None
        
        for item in attributes:
            if item["name"] == "autos.ezdate":
                year = item["value"][0]["value"] # => 2008-11
                # Retuern first 4 digits
                return year[:4]
            
    def get_first_registration(self) -> str:
        attributes = get_nested_value(self.value, ["attributes", "attribute"])

        if attributes is None:
            return None
        
        for item in attributes:
            if item["name"] == "autos.ezdate":
                return item["value"][0]["value"] # => 2008-11
        

    def get_description(self) -> str:
        description = get_nested_value(self.value, ["description", "value"])
        if description is None:
            return None

        # Remove HTML tags <br />
        description = HtmlCharacterDecoder().escape_html_tags(description)
        description = html.unescape(description)

        return description

    def get_technical_data(self):
        technical_data = []

        car_attributes = get_nested_value(self.value, ["attributes", "attribute"])

        if car_attributes is None:
            return None

        for item in car_attributes:
            if item["type"] == "BOOLEAN":
                continue
            label = item["localized-label"]
            tag = item["name"]
            unit = item["unit"]
            value = item["value"][0]["localized-label"]
            if unit:
                value = value + " " + unit.upper()

            if tag == "autos.anzahl_tueren":
                value = value + " " + "Türen"

            if tag == "autos.ezdate":
                month = item["value"][0]["value"][5:7]
                year = item["value"][0]["value"][:4]
                value = month + "/" + year

            if tag ==  "autos.shift" and value == "Manuell":
                value = "Schaltgetriebe"

            technical_data.append({"label": label, "tag": tag, "value": value})

        return technical_data

    def get_equipment(self):
        equipment = []

        # car_attributes = self.value["attributes"]["attribute"]

        car_attributes = get_nested_value(self.value, ["attributes", "attribute"])

        if car_attributes is None:
            return None
        
        for item in car_attributes:
            if item["type"] != "BOOLEAN":
                continue

            label = item["localized-label"]

            equipment.append(label)

        return equipment

    def get_phone_numbers_with_streng_format(self, text) -> list:
        phones = []
        
        phone_with_minus_regex = r"\d{4}.-.\d{7,8}"
        phone_with_minus = re.findall(phone_with_minus_regex, text)
        
        # append phone_with_minus to phones
        for phone in phone_with_minus:
            phones.append(phone)
        
        """
        Create regex for phone number +49 (0) 30 / 25 20 27 07
        in text

            Rechtliche Angaben X
            MOSHAMMER GROUP
            Inh. A. Ekici
            Otto-Suhr-Allee 97 / 99
            10585 Berlin / Germany
            Phone: +49 (0) 30 / 25 20 27 07
            E-Mail: info@moshammer.com
            USt-ID DE228829611
        """ 
        phone_with_spaces_regex = r"\+49 \(0\) \d{2} \/ \d{2} \d{2} \d{2} \d{2}"
        phone_with_spaces = re.findall(phone_with_spaces_regex, text)

        # append phone_with_spaces to phones
        for phone in phone_with_spaces:
            phones.append(phone)

        return phones

    def get_phone_numbers_with_spaces(self, text) -> list:
        regex = r"([0-9]+( [0-9])+)"

        matches = re.findall(regex, text)
        phones = []
        for match in matches:
            phones.append(match[0])

        remove_spaces = [phone.replace(" ", "") for phone in phones]
        return remove_spaces

    def get_phone_numbers_by_regex(self, input_text) -> list:
        input_text = input_text.replace("-", "")
        input_text = input_text.replace(" ", "")
        phone_regex = r"\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s\/]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{5,9}"
        phones = re.findall(phone_regex, input_text)

        if len(phones) == 0:
            text_without_slash = input_text.replace("/", "")
            phones = re.findall(phone_regex, text_without_slash)
            
        if len(phones) == 0:
            phones = self.get_phone_numbers_with_streng_format(input_text)

        if len(phones) == 0:
            phones = self.get_phone_numbers_with_spaces(input_text)

        # remove phone numbers with more than 15 digits
        phones = [phone for phone in phones if len(phone) <= 15]

        # remove phone with dot in the middle (its not a phone number, maybe date or price)
        phones = [phone for phone in phones if "." not in phone]

        # remove spaces and - from phone numbers
        phones = [phone.replace(" ", "").replace("-", "").replace("/", "") for phone in phones]

        # remove phones that don't start with +49 or 0
        phones = [phone for phone in phones if phone.startswith("+49") or phone.startswith("0")]

        return phones

    def get_seller_phones(self) -> list:
        phone_numbers = []

        description = self.get_description()

        # I got in description sometimes \xa0 instead of space, remove it

        if description is not None:
            description = description.replace("\xa0", " ")
            decription_phone_numbers = self.get_phone_numbers_by_regex(description)
            phone_numbers.extend(decription_phone_numbers)

        # Hidden phone
        try:
            hidden_phone = self.get_phone_numbers_by_regex(self.value["phone"]["value"])
            phone_numbers.extend(hidden_phone)
        except KeyError:
            pass

        # Imprint/Rechtliche Angaben
        try:
            imprint = self.value["imprint"]["value"]
            imprint_phones = self.get_phone_numbers_by_regex(imprint)
            phone_numbers.extend(imprint_phones)
        except KeyError:
            pass
        
        return phone_numbers

    def get_contact_name(self):
        try:
            return self.value["contact-name"]["value"]
        except KeyError:
            return None
    
    def get_contact_active_since(self):        
        active_since = get_nested_value(self.value, ["user-since-date-time", "value"])
        
        if active_since is None:
            return None
        
        # Convert 2022-01-12 to 12.01.22
        date = active_since[:10]
        formated_date = date[8:10] + "." + date[5:7] + "." + date[2:4]

        return formated_date

    def get_seller_type(self):
        try:
            account_type = self.value["seller-account-type"]["value"]
            account_type_unified = Unifier().unify(account_type)
            
            return Translater('DE', 'EN').translate(account_type_unified)
        except KeyError:
            return None

    def get_postal_code(self):
        return get_nested_value(self.value, ["ad-address", "zip-code", "value"])

    def get_city(self):
        return get_nested_value(self.value, ["ad-address", "state", "value"])

    def get_photo_urls(self):
        photo_urls = []

        try:
            link_objects = self.value["pictures"]["picture"]
        except KeyError:
            return []

        for link_object in link_objects:
            links = link_object["link"]
            for link in links:
                if link["rel"] == "extraLarge":
                    photo_urls.append(link["href"])
                    break

        return photo_urls

    def has_full_service_history(self) -> bool:
        attributes = get_nested_value(self.value, ["attributes", "attribute"])

        if attributes is None:
            return None

        for item in attributes:
            if item["name"] == "autos.full_service_history":
                if item["value"][0]["value"] == "true":
                    return True

        return False
    
    def has_car_accident(self) -> bool:
        attributes = get_nested_value(self.value, ["attributes", "attribute"])
        
        if attributes is None:
            return None

        for item in attributes:
            if item["name"] == "autos.schaden":
                if item["value"][0]["value"] == "ja":
                    return True

        return False