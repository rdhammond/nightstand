#!/usr/bin/python
import lxml
import lxml.cssselect
import requests

from lxml import html
from lxml.cssselect import CSSSelector

URL = 'https://oaspub.epa.gov/enviro/uv_search_v2'
SELECTOR = CSSSelector('a[href="//www3.epa.gov/enviro/facts/uv/uv_descriptions.html"] img')

class SunIntensityFeed:
	def __init__(self, longitude, latitude):
		self.body = {
			'minx': longitude,
			'miny': latitude,
			'maxx': longitude,
			'maxy': latitude
		}

	def get(self):
		page = requests.get(URL, self.body)
		tree = html.fromstring(page.content)
		element = SELECTOR(tree)[0]
		uv_index = element.get('alt').split(' ')[1]
		return int(uv_index)
