# This script will list the possible trades and the benefit you'll get
# if you sell a certain amount of cryptocurrencies and buy another currency
# considering you bought your cryptocurrency some specified time ago.
#
# The list of available cryptocurrencies is readed from a config file.

import sys
import time
import datetime
import requests
import numpy as np

args = sys.argv
amount = args[1]
currency = args[2]
date0 = args[3]

if len(args) <= 2:
	print('ERROR: Dame <cantidad> <moneda> <fecha> ')
	exit()

print("hoy es: ")
print(time.time())
print(datetime.datetime.now())

t0 = datetime.datetime.strptime(date0,"%Y-%m-%d-%H:%M")
t1 = datetime.datetime.now()

print("Desde la fecha dada han pasado:")
print(t1 - t0)


# Obtener lista de monedas
with open("config/list_currencies.list") as f:
	currencies = f.readlines()
currencies = [x.strip() for x in currencies]
N = len(currencies)
N = 7

curr_text = ""
for i in range(N):
	curr_text = curr_text + currencies[i] + ","
curr_text = curr_text[:-1]


url_init="https://min-api.cryptocompare.com/data/pricehistorical"
url_request = url_init + "?" + "fsym=" + currency + "&tsyms=" + curr_text + "&ts=" + str(int(t0.timestamp()))
print(url_request)
#https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=USD,BTC,LTC,ETH,ETC,ZEC&ts=1510599600
prices_0 = np.asarray(list(requests.get(url_request).json().get(currency).values()))

url_request = url_init + "?" + "fsym=" + currency + "&tsyms=" + curr_text + "&ts=" + str(int(t1.timestamp()))
prices_1 = np.asarray(list(requests.get(url_request).json().get(currency).values()))

price_change = (prices_1 - prices_0)/prices_0 * 100.0

print("monedas")
print(currencies[0:N-1])
print(prices_0)
print(prices_1)
print(price_change)
