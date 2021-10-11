import requests
from pprint import pprint
import os

key = os.environ.get('WEATHER_KEY')
url = 'https://api.openweathermap.org/data/2.5/weather'

def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print('error getting weather')
    else:
        current_temp = get_temp(weather_data)
        print(f'current temp os {current_temp}C')

def get_location():
    city, country = '', ''
    while len(city) == 0:
        city = input('Enter the city: ').strip()

    while len(country) != 2 or not country.isalpha():
        country = input('Enter 2-letter country code: ')

    location = f'{city},{country}'
    return location



def get_current_weather(location, key):
    try:
        query = {'q': location, 'units': 'metric', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status() # Raise exception for 400/500 errors
        data = response.json() # this may cause an error if response is not json
        return data, None
    except Exception as ex:
        print(ex)
        print(response.text)
        return None, ex


def get_temp(weather_data):
    try:
        temp = weather_data['main']['temp']
        return temp
    except KeyError:
        print('This data is not in the format expected')
        return 'Unknown'

if __name__ == '__main__':
    main()