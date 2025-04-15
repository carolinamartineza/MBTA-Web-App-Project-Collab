import os
from dotenv import load_dotenv
import urllib.request
import urllib.parse
import json
from urllib.parse import quote

# Load environment variables
load_dotenv()

# Get API keys from environment variables
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

# Useful base URLs (you need to add the appropriate parameters for each API request)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_lng() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return json.loads(data)


def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    place_encoded = urllib.parse.quote(place_name)
    url = build_mapbox_url(place_name)
    data = get_json(url)

    try:
        coordinates = data["features"][0]["geometry"]["coordinates"]
        longitude, latitude = coordinates
        return str(latitude), str(longitude)
    except (IndexError, KeyError):
        return None


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = (
    f"{MBTA_BASE_URL}?"
    f"api_key={MBTA_API_KEY}"
    f"&filter[latitude]={latitude}"
    f"&filter[longitude]={longitude}"
    f"&sort=distance"
    )

    data = get_json(url)

    try:
        stop = data["data"][0]["attributes"]
        station_name = stop["name"]
        wheelchair_accessible = stop["wheelchair_boarding"] == 1
        return station_name, wheelchair_accessible
    except (IndexError, KeyError):
        return None


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    location = get_lat_lng(place_name)
    if not location:
        return None
    
    latitude, longitude = location

    station_info = get_nearest_station(str(latitude), str(longitude))
    if not station_info:
        return None
    
    station_name, accessible = station_info
    return station_name, accessible, latitude, longitude

def build_mapbox_url(place_name: str) -> str:
    """Returns a full URL for querying the Mapbox Geocoding API with the given place name"""
    encoded_place = quote(place_name)
    return f"{MAPBOX_BASE_URL}/{encoded_place}.json?access_token={MAPBOX_TOKEN}"


def main():
    """
    You should test all the above functions here
    """
    latitude = "42.3601"
    longitude = "-71.0589"

    print("Testing get_nearest_station with Boston coordinates:")
    result = get_nearest_station(latitude, longitude)
    if result:
        station, accessible = result
        print(f"Nearest stop: {station} | Wheelchair Accessible: {'Yes' if accessible else 'No'}")
    else:
        print("No nearby station found.")

    print("Testing build_mapbox_url:")
    print(build_mapbox_url(place))

    result = find_stop_near(place)
    if result:
        station, accessible = result
        access_text = "is" if accessible else "is NOT"
        print(
            f"The nearest MBTA stop to '{place}' is '{station}' and it {access_text} wheelchair accessible."
        )
    else:
        print("Could not find a nearby stop.")

if __name__ == "__main__":
    main()
