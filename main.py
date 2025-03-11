from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()


sheet_data = data_manager.get_sheet_data()
pprint(sheet_data)

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_iataCode(row["city"])
    print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_aita_codes()




