import os 
import sys
import requests 
import pandas as pd
from requests_html import HTML

BASE_DIR = os.path.dirname(__file__)


def url_to_text(url, filename='world.html', save=False):
	r = requests.get(url)
	if r.status_code ==200:
		html_text = r.text 
		if save:
			with open(f'world{year}.html', 'w') as f:
				f.write(html_text)
		return html_text
	return None


def parse_and_extract(url, name='2021'):
	html_text = url_to_text(url)
	if html_text == None:
		return False
	r_html = HTML(html_text)
	


if __name__ == '__main__':
