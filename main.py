"""
    Working with API in python
    https://en.wikipedia.org/wiki/API
    https://docs.python-requests.org/en/latest/
    http://open-notify.org/Open-Notify-API/ISS-Location-Now/
    https://sunrise-sunset.org/api

    https://www.journaldev.com/23324/python-strftime
"""
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
# if response ok, it will return [200]

# if response.status_code == 404:
#     raise Exception("That resources does not exists")
# elif response.status_code == 401:
#     raise Exception("You are not authorize to access this site")
#
# Above code can replace with
#   response.raise_for_status()

data = response.json()
print(data)
# example output : {'timestamp': 1650768037, 'iss_position': {'latitude': '17.9467', 'longitude': '157.2683'}, 'message': 'success'}

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (longitude, latitude)
print(iss_position)

import datetime as dt

my_latitude = 3.1634051
my_longitude = 101.6936846
parameters = {
    "lat" : my_latitude,
    "lng" : my_longitude,
    "formatted" : 0
}

sunposition_api_url = f"https://api.sunrise-sunset.org/json"
"""
Parameters
    lat (float): Latitude in decimal degrees. Required.
    lng (float): Longitude in decimal degrees. Required.
    date (string): Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats. 
        If not present, date defaults to current date. Optional.
    callback (string): Callback function name for JSONP response. Optional.
    formatted (integer): 0 or 1 (1 is default). 
        Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds. Optional.
"""
print(sunposition_api_url)
response = requests.get(sunposition_api_url, params=parameters, verify=False)
response.raise_for_status()
print(response.json())

timenow = dt.datetime.now()
print(f"now : {timenow}")

sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]
print(f"UTC sunrise : {sunrise}, sunset : {sunset}")

kl_sunrise = dt.datetime.strptime(sunrise[:19], "%Y-%m-%dT%H:%M:%S") + dt.timedelta(hours=8)
kl_sunset = dt.datetime.strptime(sunset[:19], "%Y-%m-%dT%H:%M:%S") + dt.timedelta(hours=8)
print(f"KL sunrise : {kl_sunrise}, sunset : {kl_sunset}")
