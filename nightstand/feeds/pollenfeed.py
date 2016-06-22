#!/usr/bin/python
import lxml
import lxml.cssselect
import requests

from lxml import html
from lxml.cssselect import CSSSelector

URL = 'https://www.wunderground.com/DisplayPollen.asp'
SELECTOR = CSSSelector('.pollen-table .levels p')

class PollenFeed:
	def __init__(self, zipcode):
		self.queryparams = {
                        'Zipcode': zipcode,
                        'MR': 1
                }

	def get(self):
		page = requests.get(URL, self.queryparams)
		tree = html.fromstring(page.content)
		value = SELECTOR(tree)[0].text_content()
		return float(value)
