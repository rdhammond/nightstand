#!/usr/bin/python
import lxml
import lxml.cssselect
import requests

from lxml import html
from lxml.cssselect import CSSSelector

URL = 'http://pollen.aaaai.org/nab/index.cfm?p=allergenreport'
SELECTOR = CSSSelector('.nabCount img')

class PollenFeed:
	def __init__(self, station_id):
		self.station_id = station_id
		self.url = URL
		self.body = { 'lng': 'en-US', 'stationid': station_id }

	def get(self):
		page = requests.post(self.url, self.body)
		tree = html.fromstring(page.content)
		elements = SELECTOR(tree)
		feed_sum = 0

		for e in elements:
			src = e.get('src')

			if 'low.gif' in src:
				feed_sum += 2.5
			elif 'moderate.gif' in src:
				feed_sum += 5
			elif 'high.gif' in src:
				feed_sum += 7.5
			elif 'veryhigh.gif' in src:
				feed_sum += 10

		avg = float(feed_sum) / len(elements)
		return round(avg, 1)
