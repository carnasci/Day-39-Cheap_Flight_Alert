import os
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
from credentials import sheet_auth
from dotenv import load_dotenv

load_dotenv()


SHEET_URL = "https://api.sheety.co/acce13247ad2cc699293ff3d1ff26f90/cheapFlightsAlert/prices"


class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = []

    def get_sheet_data(self):
        sheet_response = requests.get(url=SHEET_URL, auth=self._authorization)
        data = sheet_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

