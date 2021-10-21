import requests
import json


class ApiRequest:
    url: str

    def __init__(self, url: str):
        self.url = url

    def make_request(self) -> dict or list:
        response = requests.get(self.url)
        raw_data = response.text
        parsed_data = json.loads(raw_data)
        return parsed_data
