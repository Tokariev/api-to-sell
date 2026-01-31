class Translater(object):
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def translate(self, text):
        if text == "PRIVATE":
            return "Privat"
            
        if text == "COMMERCIAL":
            return "Gewerblich"
    
        if text == "PrivateSeller":
            return "Privat"
        
        if text == "Dealer":
            return "Händler"
        
        return text