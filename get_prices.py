#!/usr/bin/python

import sys
import requests
from engineering_notation import EngUnit as EngUnit

def eng(str_units):
	return str(EngUnit(str_units))


args = sys.argv

if len(args) <= 1:
	print('ERROR: Dame una criptomoneda valida')
	exit()

coin = args[1]

url_api = 'https://api.coinmarketcap.com/v1/ticker/'
url 	= url_api + coin
r = requests.get(url).json()[0]
symbol = r.get('symbol')
price_usd = r.get('price_usd')+' USD'
price_btc = r.get('price_btc')+'BTC'

if len(args) == 2:
	print("1 ", symbol, " = ", eng(price_usd), sep='')

elif len(args) == 3:
	time_change = args[2]
	times = ['1h', '24h', '7d']
	if time_change in times:
		change = r.get('percent_change_' + args[2])
		print("1 ", symbol, " = ", eng(price_usd), " (", time_change, ": ", change, "%)", sep='')
	else:
		print('ERROR: argumento de tiempo invalido. Use (1h, 24h, 7d)')
		exit()
