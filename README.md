# WeatherBot with LangChain Tool Use

This application is a demonstration of using LangChain and Streamlit to create a simple weather bot. The bot fetches current weather data for a specified location using the OpenWeather API and processes user queries with a LangChain agent powered by OpenAI's GPT-4 model.

## Features

- Fetches current weather data for any location using the OpenWeather API.
- Utilizes LangChain to process natural language queries.
- Built with Streamlit for an interactive web interface.

## Prerequisites

- Docker installed on your machine.
- OpenWeather API key.
- OpenAI API key.

## Building the Docker Image

To build the Docker image for this application, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the directory containing the `Dockerfile`.
3. Run the following command to build the Docker image:

   ```bash
   docker build -t weatherbot .
   ```

## Running the Docker Container

Once the Docker image is built, you can run the application in a container with the following steps:

1. Ensure your OpenWeather and OpenAI API keys are set as environment variables:

   ```bash
   export OPENWEATHER_API_KEY=your_openweather_api_key
   export OPENAI_API_KEY=your_openai_api_key
   ```

2. Run the Docker container using the command:

   ```bash
   docker run -p 8501:8501 -e OPENWEATHER_API_KEY -e OPENAI_API_KEY weatherbot
   ```

3. Open your web browser and go to `http://localhost:8501` to access the application.

## Usage

- Enter a weather-related question in the input field.
- Click the "Get Weather" button to fetch the weather information.
- The application will display the current weather for the specified location.

Enjoy using the WeatherBot to get real-time weather updates!