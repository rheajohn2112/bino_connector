# 🌐 Bino Connector API

A lightweight Flask-based backend API that connects with external services like NewsAPI and OpenWeather to fetch real-time information and return clean, formatted responses.
This service is designed as the backend connector for the Bino Application.

---

## 🚀 Features
## 🔍 Fetch Top News

Endpoint: POST /search

Body:

{ "query": "technology" }


Returns: Top 5 news article titles.

## ☁️ Fetch Weather Details

Endpoint: POST /weather

Body:

{ "city": "London" }


Returns: Weather description, temperature, and humidity.

## 📁 Project Structure
BINO_CONNECTOR/
│── .venv/
│── bino_connector/
│   ├── app.py
│   ├── .env               # ignored using .gitignore
│── requirements.txt
│── Procfile
│── .gitignore
│── README.md

## 🔧 Environment Variables

Create a .env file inside bino_connector/:

NEWS_API_KEY=your_news_api_key
WEATHER_API_KEY=your_weather_api_key

## 📌 API Usage Examples
1️⃣ Search News

POST /search
Body:

{
  "query": "technology"
}


Sample Response:

{
  "results": "Here are the top results:\n1. ..."
}

2️⃣ Get Weather

POST /weather
Body:

{
  "city": "London"
}


Sample Response:

{
  "weather": "Weather: clear sky\nTemperature: 25°C\nHumidity: 60%"
}

## ▶️ Running the App Locally
pip install -r requirements.txt
python bino_connector/app.py

## 🚀 Deployment

This project includes a Procfile, making it easy to deploy on:

Render

Railway

Heroku

Any Python hosting service
