import os
import requests
from ddgs import DDGS

# Load API keys
GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

from ddgs import DDGS

def get_hotels(city: str):
    return [
        f"Taj Hotel {city}",
        f"Grand Palace {city}",
        f"Budget Inn {city}"
    ]

def get_weather(city: str):
    return f"{city}: Warm weather, around 25-32°C"

def search_places(query: str):
    with DDGS() as ddgs:
        results = [r["title"] for r in ddgs.text(query, max_results=5)]
    return results
