from agent.travel_utils import get_hotels, get_weather, search_places

def hotel_finder_tool(city: str) -> str:
    """Find hotels in the given city."""
    try:
        hotels = get_hotels(city)
        return "\n".join([f"{h['name']} - {h['address']}" for h in hotels])
    except Exception as e:
        return f"Hotel API error: {e}"

def weather_tool(city: str) -> str:
    """Get the current weather of the given city."""
    try:
        return get_weather(city)
    except Exception as e:
        return f"Weather API error: {e}"

def search_tool(query: str) -> str:
    """Search for restaurants or attractions."""
    try:
        results = search_places(query)
        return "\n".join(results)
    except Exception as e:
        return f"Search API error: {e}"
