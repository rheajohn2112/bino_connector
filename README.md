Bino Connector API

A simple Flask-based API that connects with external services like News API and Weather API to fetch information and return clean, formatted results.
This project is designed to act as a backend connector for the Bino application.

🚀 Features
✔ Fetch Top News

Endpoint: /search

Method: POST

Send a JSON body with a query

Returns top 5 news article titles

✔ Fetch Weather Details

Endpoint: /weather

Method: POST

Send a JSON body with a city

Returns weather description, temperature, and humidity

🧩 Project Structure
BINO_CONNECTOR/
│── .venv/
│── bino_connector/
│   ├── app.py
│   ├── .env   (ignored using .gitignore)
│── requirements.txt
│── Procfile
│── .gitignore
│── README.md   <-- (this file)

🔧 Environment Variables

Create a .env file inside the project folder:

NEWS_API_KEY=your_news_api_key
WEATHER_API_KEY=your_weather_api_key


⚠ Never commit .env — it is added to .gitignore.

📌 API Usage Examples
1️⃣ Search News

POST /search

Request body:

{
  "query": "technology"
}


Response:

{
  "results": "Here are the top results:\n1. ..."
}

2️⃣ Get Weather

POST /weather

Request body:

{
  "city": "London"
}


Response:

{
  "weather": "Weather: clear sky\nTemperature: 25°C\nHumidity: 60%"
}

▶️ Running the App Locally
pip install -r requirements.txt
python bino_connector/app.py

🚀 Deployment

This project includes a Procfile so you can deploy to platforms like Render / Railway / Heroku easily.