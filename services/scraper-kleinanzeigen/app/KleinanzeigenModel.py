import re


class KleinanzeigenModel(object):
    def __init__(self, barnd, title):
        self.brand = barnd
        self.title = title
    
    def get_model(self):
        # split brand by space
        model = self.title
        
        if not self.brand:
            return model
        
        brand_words = self.brand.split(" ")

        # remove brand_words from title
        for brand_word in brand_words:
            # find position of brand_word in title
            start_index = model.lower().find(brand_word.lower())
            if start_index == -1:
                continue
            end_index = start_index + len(brand_word)
            # remove brand_word from title
            model = model[:start_index] + model[end_index:]

        for brand_word in brand_words:
            if brand_word == "Volkswagen":
                start_index = model.lower().find('volkswagen')
                if start_index == -1:
                    continue
                end_index = start_index + len('volkswagen')
                model = model[:start_index] + model[end_index:]

        for brand_word in brand_words:
            if brand_word.lower() == "citroen":
                start_index = model.lower().find('citroën')
                if start_index == -1:
                    continue
                end_index = start_index + len('citroën')
                model = model[:start_index] + model[end_index:]

        # remove VW from title
        start_index = model.lower().find('vw')
        if start_index != -1:
            end_index = start_index + len('vw')
            model = model[:start_index] + model[end_index:]

        # remove all non-alphanumeric characters at the beginning
        return re.sub(r"^[^a-zA-Z0-9]+", "", model)

