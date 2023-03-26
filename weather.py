import sys
import os
import requests

class WeatherForecast:
    def __init__(self, key, url):
        self.key = key
        self.url = url

    def importData(self, key):
        querystring = {"units":"auto","lang":"en"}

        headers = {
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "dark-sky.p.rapidapi.com"
        }

        response = requests.get(url)

        return response.text

    def analyseData(self):
        pass

url = "https://dark-sky.p.rapidapi.com/%7Blatitude%7D,%7Blongitude%7D"
key = sys.argv[1]
# queryData = sys.argv[2]

data = WeatherForecast(key, url)

newDataa = data.importData(key)

print(newDataa)




# key = sys.argv[1]
# requestedWeather = sys.argv[2]

# if os.path.exists(''):
#     pass