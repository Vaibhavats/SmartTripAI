import os
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_community.llms import Ollama  # (You can switch to langchain_ollama later)
from agent.travel_tools import hotel_finder_tool, weather_tool, search_tool  # updated tools

# Initialize LLM (Ollama)
llm = Ollama(model="mistral")

# Define tools
tools = [
    Tool(
        name="HotelFinder",
        func=hotel_finder_tool,
        description="Find hotels in a city."
    ),
    Tool(
        name="Weather",
        func=weather_tool,
        description="Get current weather of a city."
    ),
    Tool(
        name="Search",
        func=search_tool,
        description="Search for restaurants or attractions in a city."
    )
]

# Initialize Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def plan_trip(user_input: str) -> str:
    """
    Plan a trip based on user input using LangChain agent.
    Now uses .invoke() instead of deprecated .run().
    """
    try:
        result = agent.invoke({"input": user_input})
        return result["output"]
    except Exception as e:
        return f"Error while planning trip: {e}"


if __name__ == "__main__":
    print("SmartTripAI Planner is running...")
    query = input("Where would you like to plan your trip? ")
    print(plan_trip(query))
