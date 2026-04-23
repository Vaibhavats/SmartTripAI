import os
from duckduckgo_search import DDGS
from dotenv import load_dotenv

# Load environment variables from root
load_dotenv()

from agent.planner import plan_trip

if __name__ == "__main__":
    user_input = input("Enter your trip: ")
    result = plan_trip(user_input)
    print(result)