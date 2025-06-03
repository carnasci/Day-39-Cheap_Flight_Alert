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
        """
                Retrieves the IATA code for a specified city using the Amadeus Location API.
                Parameters:
                city_name (str): The name of the city for which to find the IATA code.
                Returns:
                str: The IATA code of the first matching city if found; "N/A" if no match is found due to an IndexError,
                or "Not Found" if no match is found due to a KeyError.

                The function sends a GET request to the IATA_ENDPOINT with a query that specifies the city
                name and other parameters to refine the search. It then attempts to extract the IATA code
                from the JSON response.
                - If the city is not found in the response data (i.e., the data array is empty, leading to
                an IndexError), it logs a message indicating that no airport code was found for the city and
                returns "N/A".
                - If the expected key is not found in the response (i.e., the 'iataCode' key is missing, leading
                to a KeyError), it logs a message indicating that no airport code was found for the city
                and returns "Not Found".
                """

        api_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        header = {
            "Authorization" : f"Bearer {self._token}"
        }
        query = {
            "keyword" : city_name,
            "max" : "2",
            "include" : "AIRPORTS",
        }
        response = requests.get(
            url=api_endpoint,
            params=query,
            headers=header,
        )
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")

        try:
            data = response.json()["data"]
            code = data[0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code
