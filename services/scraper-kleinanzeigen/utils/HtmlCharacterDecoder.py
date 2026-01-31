
# Create class to escape HTML characters
from bs4 import BeautifulSoup


class HtmlCharacterDecoder:
   
    def __init__(self):
        self.html_codes = (
            ('&#39;', "'"),
            ('&#x2F;', "/"),
            ('&#x5c;', "\\"),
            ('&quot;', '"'),
            ('&gt;', '>'),
            ('&lt;', '<'),
            ('&amp;', '&'),
            ('&#x27;', "'"),
        )
   
    def escape_html_codes(self, text):
        if text is None:
            return None

        for code in self.html_codes:
            text = text.replace(code[0], code[1])
        return text
    
    def escape_html_tags(self, text):
        if text is None:
            return None
        
        soup = BeautifulSoup(text, 'html.parser')
        text_without_html_tags = soup.get_text(separator=' ')
        
        return text_without_html_tags