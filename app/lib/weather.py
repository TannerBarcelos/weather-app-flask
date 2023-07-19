"""
Weather Module
"""
from flask import current_app
from pprint import pprint
import requests
import os

"""
This function will get the current weather for a given city

Parameters
----------
city: str
    The city to get the weather for
"""

def get_current_weather(city='Honolulu'):
    """
    This function will get the current weather for a given city
    """ 
    url = request_builder(city)
    response = requests.get(url).json()
    pprint(response)
    return response


def request_builder(city='Honolulu'):
    """
    This function will build the request URL for the Open Weather API
    """
    api_key = current_app.config['OPEN_WEATHER_API_KEY']
    base_url = current_app.config['OPEN_WEATHER_BASE_URL']
    return f"{base_url}?q={city}&units=imperial&appid={api_key}"

# Using as a script rather than a module / flask app
if __name__ == "__main__":
    city = input('Enter a city to get weather for: ').strip()

    # If user does not enter a city, intercept the empty string and use San Jose as the default
    if not city:
        city = 'Honolulu'

    get_current_weather(city)