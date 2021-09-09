import requests

api_key =

clave_api = ''

headers = {
	
	'Accepts':'application/json',
	'X-CMC_PRO_API_KEY':clave_api
}


r = requests.get(endpoint, headers=headers)