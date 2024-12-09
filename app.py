import streamlit as st
import requests
import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

# Load API keys from environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENWEATHER_API_KEY or not OPENAI_API_KEY:
    raise ValueError("API keys are missing. Set OPENWEATHER_API_KEY and OPENAI_API_KEY in your environment variables.")

# Define a tool to fetch weather data
def fetch_weather_tool(location: str) -> str:
    """Fetch current weather data for the specified location in imperial units."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The current weather in {location} is {weather} with a temperature of {temperature}°F."
    else:
        return "Unable to fetch weather data. Please check the location name."

# Initialize LangChain tools
weather_tool = Tool(
    name="Weather Fetcher",
    func=fetch_weather_tool,
    description="Use this tool to get the current weather for a specified location."
)

# Initialize LangChain agent
chat_model = ChatOpenAI(temperature=0, model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
tools = [weather_tool]
agent = initialize_agent(tools, chat_model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Streamlit application
def main():
    st.title("WeatherBot with LangChain Tool Use")
    st.write("Ask a weather-related question, and I'll fetch the answer for you!")

    # User input
    user_question = st.text_input("Your question:")

    if st.button("Get Weather"):
        if user_question:
            # Pass user question to the LangChain agent
            response = agent.run(user_question)
            st.write(response)
        else:
            st.write("Please enter a weather-related question.")

if __name__ == "__main__":
    main()