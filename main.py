import os
from dotenv import load_dotenv

# Load .env from the project root (i.e., SmartTripAI/.env)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# DEBUG (optional): Print API key
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

from agent.planner import plan_trip

if __name__ == "__main__":
    user_input = "Plan my weekend trip to Delhi with vegetarian food preference"
    result = plan_trip(user_input)
    print(result)
