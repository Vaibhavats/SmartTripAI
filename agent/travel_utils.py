import os
import requests
from duckduckgo_search import DDGS

# Load API keys
GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_hotels(city: str):
    url = f"https://api.geoapify.com/v2/places?categories=accommodation.hotel&text={city}&limit=5&apiKey={GEOAPIFY_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(response.text)
    data = response.json()
    hotels = []
    for feature in data.get("features", []):
        name = feature["properties"].get("name", "Unknown Hotel")
        address = feature["properties"].get("formatted", "No address")
        hotels.append({"name": name, "address": address})
    return hotels

def get_weather(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(response.text)
    data = response.json()
    return f"Weather in {city}: {data['weather'][0]['description']}, {data['main']['temp']}°C"

def search_places(query: str):
    with DDGS() as ddgs:
        results = [r["title"] + " - " + r["href"] for r in ddgs.text(query, max_results=5)]
    return results
