import re

class ExternalCarID:

    def extract_id_by_url(self, url: str) -> str:
        # 1. Identify the platform
        if 'kleinanzeigen' in url:
            return self.__extract_id_from_kleinanzeigen(url)
        else:
            return 'Not implemented'


    def __extract_id_from_kleinanzeigen(self, url: str) -> str:
        match = re.search(r'/(\d{10})', url)
        return match.group(1) if match else ""