import requests
import urllib3

# DISABLE SSL WARNING
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def fetch_weather(city):

    city_coordinates = {
        "Delhi": (28.61, 77.20),
        "Mumbai": (19.07, 72.87),
        "Patiala": (30.34, 76.38),
        "Chandigarh": (30.74, 76.79),
        "Bangalore": (12.97, 77.59)
    }

    lat, lon = city_coordinates.get(city, (28.61, 77.20))

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        "&hourly=temperature_2m,"
        "relative_humidity_2m,"
        "precipitation,"
        "wind_speed_10m"
    )

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        verify=False,
        timeout=20
    )

    data = response.json()

    return data