import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.api_key = os.environ["AMADEUS_KEY"]
        self.api_secret = os.environ["AMADEUS_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type" : "client_credentials",
            "client_id" : self.api_key,
            "client_secret" : self.api_secret,
        }
        response = requests.post(
            url="https://test.api.amadeus.com/v1/security/oauth2/token",
            headers=header,
            data=body,
            )
        data = response.json()
        print(f"Your token is {data['access_token']}")
        print(f"Your token expires in {data['expires_in']} seconds")
        return data["access_token"]

    def get_iataCode(self, city_name):
        code = "TESTING"
        return code
