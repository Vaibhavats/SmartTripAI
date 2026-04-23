from langchain_community.llms import Ollama
import re

from agent.travel_tools import hotel_finder_tool, weather_tool, search_tool

# LLM
llm = Ollama(model="mistral")

# Extract city
def extract_city(user_input: str):
    match = re.search(r"to ([a-zA-Z ]+)", user_input.lower())
    if match:
        return match.group(1).strip().title()
    return "India"

# Main function
def plan_trip(user_input: str) -> str:
    try:
        city = extract_city(user_input)

        weather = weather_tool(city)
        hotels = hotel_finder_tool(city)
        places = search_tool(city)

        prompt = f"""
Plan a 2-3 day trip to {city}.

Weather: {weather}
Hotels: {hotels}
Places: {places}

IMPORTANT:
- Always include weather
- Always include hotels
- Do not mention API errors

Format:

📍 {city} Trip Plan

🌦 Weather:
{weather}

🏨 Hotels:
{hotels}

📅 Day-wise Itinerary:
Day 1:
Day 2:
"""

        response = llm.invoke(prompt)
        return response

    except Exception as e:
        return f"Error: {e}"