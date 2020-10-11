import os
import json

from urllib import request
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv("OWM_TOKEN")

def kelvin_to_celsius(temp_k):
    #kelvin = -273.15
    return -273.15 + temp_k

# def print_current_weather_info(weather):
#     # TODO

# def print_forecast_info(weather):
#     # TODO

def fetch_current_weather(city):
    with request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_token}') as response:
        weather = response.read()
        weatherData = json.loads(weather)
    return weatherData

def fetch_forecast(city, days_count):
    with request.urlopen(f'http://api.openweathermap.org/data/2.5/forecast?q={city}&cnt={days_count}&appid={api_token}') as response:
        weather = response.read()
    return weather

#print(kelvin_to_celsius(10))
print(type(fetch_current_weather('Helsinki')))
#print(fetch_forecast('Helsinki', 2))
