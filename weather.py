import requests
from kivy.logger import Logger

API_KEY = "0da2c36427d04c2b219d5791dc08e90a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for a given city and return formatted string"""
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        weather_info = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'].title(),
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        
        return (f"Temperature: {weather_info['temperature']}°C\n"
                f"Weather: {weather_info['description']}\n"
                f"Humidity: {weather_info['humidity']}%\n"
                f"Wind Speed: {weather_info['wind_speed']} m/s")
                
    except requests.exceptions.RequestException as e:
        Logger.error(f"Weather API Error: {str(e)}")
        return "Failed to fetch weather data. Please try again."
