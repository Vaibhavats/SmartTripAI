# test_rapidapi.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("RAPIDAPI_KEY")
url = "https://hotels4.p.rapidapi.com/locations/v3/search"
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}
params = {"q": "Delhi", "locale": "en_US"}

response = requests.get(url, headers=headers, params=params)
print("Status:", response.status_code)
print("Output:", response.json())
