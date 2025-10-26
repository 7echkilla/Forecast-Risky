import requests
import pandas as pd

from datetime import datetime

def get_current_location():
    """
    Fetch current latitude and longitude based on IP address.
    """
    try:
        response = requests.get("https://ipinfo.io/json")
        response.raise_for_status()
        data = response.json()

        latitude, longitude = map(float, data["loc"].split(","))
        return latitude, longitude
    except Exception as e:
        raise RuntimeError(print_message("fail", "Could not get current location: {e}"))

def get_weather_data(latitude:float, longitude:float, start:int=None, end:int=None):
    """
    Fetch historical temperature & rainfall data from NASA POWER API (https://power.larc.nasa.gov/docs/services/api/)
    """
    if start is None:
        start = datetime.now().year
    if end is None:
        end = datetime.now().year

    url = (
        f"https://power.larc.nasa.gov/api/temporal/daily/point"
        f"?parameters=T2M,PRECTOT"
        f"&community=RE"
        f"&longitude={longitude}&latitude={latitude}"
        f"&start={start}0101&end={end}1231"
        f"&format=JSON"
    )

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(print_message("fail", "Could not fetch data"))

    json_data = response.json()["properties"]["parameter"]
    data = pd.DataFrame(json_data)
    data.replace(-999.00, pd.NA, inplace=True)

    return data

def print_message(type="info", text="Default text"):
    match type:
        case "info":
            print(f"[INFO] {text}")
        case "fail":
            print(f"\033[91m[FAIL]\033[0m {text}")
        case "pass":
            print(f"\033[92m[PASS]\033[0m {text}")
        case _:
            pass

def main():
    get_current_location()
    # get_weather_data(latitude=10.10, longitude=10.10)

if __name__ == "__main__":
    main()