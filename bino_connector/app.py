from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)

def fetch_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return []
    
    articles = response.json().get("articles", [])
    return [article["title"] for article in articles[:5]]

def format_response(results):
    if not results:
        return "Sorry, no results found."
    
    msg = "Here are the top results:\n"
    for i, r in enumerate(results, 1):
        msg += f"{i}. {r}\n"
    return msg

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return weather, temp, humidity

def format_weather(weather, temp, humidity):
    return (
        f"Weather: {weather}\n"
        f"Temperature: {temp}°C\n"
        f"Humidity: {humidity}%"
    )

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get("query")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    results = fetch_news(query)
    message = format_response(results)
    return jsonify({"results": message})

@app.route('/weather', methods=['POST'])
def weather():
    data = request.json
    city = data.get("city")

    if not city:
        return jsonify({"error": "City not provided"}), 400

    result = fetch_weather(city)

    if not result:
        return jsonify({"error": "Could not fetch weather"}), 500

    weather_desc, temp, humidity = result
    message = format_weather(weather_desc, temp, humidity)

    return jsonify({"weather": message})

if __name__ == '__main__':
    app.run(debug=True)
