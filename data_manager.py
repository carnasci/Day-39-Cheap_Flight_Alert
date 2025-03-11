import requests
from pprint import pprint
from credentials import sheet_auth


SHEET_URL = "https://api.sheety.co/acce13247ad2cc699293ff3d1ff26f90/cheapFlightsAlert/prices"
SHEET_AUTH = sheet_auth

class DataManager:

    def get_sheet_data(self):
        sheet_header = {
            "Authorization" : SHEET_AUTH,
        }
        sheet_response = requests.get(url=SHEET_URL, headers=sheet_header)
        sheet_data = sheet_response.json()
        pprint(sheet_data)

