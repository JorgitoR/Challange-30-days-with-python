import os 
import sys
import datetime
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
	r_html = HTML(html=html_text)
	table_class = '.imdb-scroll-table'
	r_table = r_html.find(table_class)

	table_data = []
	header_names =[]

	if len(r_table) == 0:
		return False

	analizar_tabla = r_table[0]
	rows = analizar_tabla.find("tr")
	header_row = rows[0]
	header_cols = header_row.find('th')
	header_names = [x.text for x in header_cols]

	for row in rows[1:]:
		cols = row.find("td")
		row_data = []
		row_dict_data = {}
		for i, col in enumerate(cols):

			header_name = header_names[i]
			row_data.append(col.text)

		table_data.append(row_data)

	df = pd.DataFrame(table_data, columns=header_names)

	path = os.path.join(BASE_DIR, 'data')
	os.makedirs(path, exist_ok=True)
	filepath = os.path.join('data', f"{name}.csv")
	df.to_csv(filepath, index=False)
	return True

def run(start_year=None, years_ago=0):
	if start_year == None:
		now = datetime.datetime.now()
		start_year = now.year()

	assert isinstance(start_year, int)
	assert isinstance(years_ago, int)
	assert len(f"{start_year}") == 4

	for i in range(0, years_ago+1):
		url = f"https://www.boxofficemojo.com/year/world/{start_year}/"

		finished = parse_and_extract(url, name=start_year)
		if finished:
			print(f"finished {start_year}")
		else:
			print(f"{start_year} not finished")

		start_year -= 1

if __name__ == "__main__":
    try:
        start = int(input())
    except:
        start = None
    try:
        count = int(input())
    except:
        count = 0
    run(start_year=start, years_ago=count)