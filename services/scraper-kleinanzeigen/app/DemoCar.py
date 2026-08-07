import json
import os
import re

DEMO_URL_PATTERN = re.compile(r"kleinanzeigen\.de/s-anzeige/demo-car/\d+-\d+-\d+")

DEMO_FILE = os.path.join(os.path.dirname(__file__), 'demo', 'demo_car.json')


class DemoCar(object):

    @staticmethod
    def matches(url: str) -> bool:
        return bool(DEMO_URL_PATTERN.search(url))

    @staticmethod
    def load() -> dict:
        with open(DEMO_FILE, 'r', encoding="utf-8") as file:
            return json.load(file)
