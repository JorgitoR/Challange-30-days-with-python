import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import pprint

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'd1b66ed9-e6fb-4adf-8e8b-482d056d88b4',
}

session = Session()
session.headers.update(headers)

try:
	response = session.get(url, params=parameters)
	data =json.loads(response.text)
	datos = data['data']
	foundCode ={}
	codigo = str(input())
	for data in datos:
		
		foundCode[data['symbol']] = 1

		if len(foundCode) > 1:

			if codigo in foundCode and data['symbol'] == codigo:
				print('Name', data['name'])
		
			elif codigo not in foundCode:
				print('el codigo', codigo, 'No existe, Introduce un codigo valido')
				codigo = str(input())

	

	cantidad = int(input())
	endpoint = f'https://api.binance.com/api/v3/ticker/price?symbol={codigo}USDT'
	url = requests.get(endpoint)
	data = url.json()
	usd = data['price']
	usd_cripto = float(usd) * cantidad
	print('Mi cripto', codigo, 'cuesta en USD', usd_cripto)



except (ConnectionError, Timeout, TooManyRedirects) as e:
	print(e)