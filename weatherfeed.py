#!/usr/bin/python
import requests

URL = 'http://forecast.io/forecast?q={lat},{long}&satellites&raw'

class WeatherFeed:
    def __init__(self, longitude, latitude):
        self.url = URL.replace('{lat}', str(latitude)).replace('{long}', str(longitude))

    def get(self):
        req = requests.get(self.url, headers={'Referer': 'http://forecast.io/'})
        data = req.json()

        temp_node = data['currently']['temperature']
        desc_node = data['currently']['summary']

        return {
            'temp': int(round(float(temp_node))),
            'weather': self.getWeatherType(desc_node)
        }

    def getWeatherType(self, desc_node):
        if 'Cloud' in desc_node:
            return 'cloudy'
        elif 'Rain' in desc_node:
            return 'rainy'
        elif 'Snow' in desc_node:
            return 'snowy'
        else:
            return 'clear'
