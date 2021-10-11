# https://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=metric&appid=25e8de269e48f95dfdc869a06098bc88
import os
import requests
from datetime import datetime
from pprint import pprint

key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis', 'units': 'metric', 'appid': key}

url = 'https://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()

pprint(data)

list_of_forecasts = data['list']

for forecast in list_of_forecasts:
    temp = forecast['main']['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    print(f'At {forecast_date} the temp is {temp}c')