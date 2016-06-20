#!/usr/bin/python
import requests
import datetime

from lxml import html
from lxml.cssselect import CSSSelector

IP_URL = 'https://www.whatismyip.com'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
IP_SELECTOR = CSSSelector('.ip > div:nth-child(1)')

LOCATION_URL = 'http://ip-api.com/json/{ip}'

SUNRISE_SUNSET_URL = 'http://api.sunrise-sunset.org/json'

class UTC(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return datetime.timedelta(0)

class GeoLocation:
    def __init__(self):
        self.ip_headers = { 'User-Agent': USER_AGENT }

    def getIp(self):
        req = requests.get(IP_URL, headers=self.ip_headers)
        page = html.fromstring(req.content)
        root = IP_SELECTOR(page)[0]
        ip = ''

        for element in root:
            ip = ip + element.text_content()

        return ip

    def getLocation(self, ip):
        url = LOCATION_URL.replace('{ip}', ip)
        req = requests.get(url)
        data = req.json()

        return {
            'latitude': data['lat'],
            'longitude': data['lon'],
            'zipcode': data['zip']
        }

    def getSunriseSunset(self, lat, lon):
        req = requests.get(SUNRISE_SUNSET_URL, {
            'lat': lat,
            'lng': lon,
            'formatted': 0
        })
        json = req.json()

        return {
            'sunrise': self.parseTime(json['results']['sunrise']),
            'sunset': self.parseTime(json['results']['sunset'])
        }

    def parseTime(self, str):
        return datetime.datetime.strptime(str, '%Y-%m-%dT%H:%M:%S+00:00')
