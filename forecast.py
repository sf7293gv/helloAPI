import os
import requests
from datetime import datetime
from pprint import pprint

key = os.environ.get('WEATHER_KEY')
url = 'https://api.openweathermap.org/data/2.5/forecast'



def show_results():
    location = get_location() # This method will pass user's input for the loation
    temp_unit = get_temp_unit() # And this will pas the user's input for the temperature unit

    """ This method will either pass a json response and None as error,
        or it will pass no response and error. If it passes and 
        error don't start program. But in the case it does, start it"""
    forecast, error = get_forecast(location, temp_unit) 
    if error:
        print('Error fetching forecast')
    else:
        """ Get the list from the json response, store it, loop over it 
            and extract the data we need so we can print the results to the user"""
        lists_of_forecasts = forecast['list'] 
        for forecastList in lists_of_forecasts:
            temp = forecastList['main']['temp']
            timestamp = forecastList['dt']
            forecast_timeNdate = datetime.fromtimestamp(timestamp)
            wind_speed = forecastList['wind']['speed']
            print(f'At {forecast_timeNdate} the temperature is {temp} and the wind speed is {wind_speed}')

   

""" This method will get the location from the user, return it so the api can show forecast for the location"""
def get_location():
    city, country = '', ''
    while len(city) == 0:
        city = input('Enter the city: ').strip()

    while len(country) != 2 or not country.isalpha():
        country = input('Enter 2-letter country code: ')

    location = f'{city},{country}'
    return location

""" This method will get the temp unit from user and
    return it so the api can show results in that temp unit"""
def get_temp_unit():
    imperial = 'imperial'
    metric = 'metric'
    while (True):
        temp = input('Enter F for Fahrenheit or C for Celsius: ')
        temp.lower()
        if temp == 'f':
            return imperial
            
        if temp == 'c':
            return metric

""" After getting the user input, this method will get the response from 
    the api and return it if no errors occur"""
def get_forecast(location, temp_unit):
    try:
        query = {'q': location, 'units': temp_unit, 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status() # Raise an exception for 400-500 errors
        forecast = response.json()
        return forecast, None # return the forecast, and None (no errors)
    except Exception as ex:
        print(ex)
        print(response.text)
        return None, ex # None (no forecast data) ex as the error


if __name__ == '__main__':
    show_results()