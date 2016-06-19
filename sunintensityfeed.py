#!/usr/bin/python
import requests

URL = 'https://www.coppertone.com/webservice/uvindex.php'
HEADERS = { 'Accept': 'application/json' }

class SunIntensityFeed:
    def __init__(self, zipcode):
        self.body = { 'zip': zipcode }

    def get(self):
    	req = requests.get(URL, self.body, headers=HEADERS)
        data = req.json()
        return int(data['d']['Index']);
