# This script will list the possible trades and the benefit you'll get
# if you sell a certain amount of cryptocurrencies and buy another currency
# considering you bought your cryptocurrency some specified time ago.
#
# The list of available cryptocurrencies is readed from a config file.

import sys
import time
import datetime

args = sys.argv

if len(args) <= 2:
	print('ERROR: Dame <cantidad> <moneda> <fecha> ')
	exit()

print("hoy es: ")
print(time.time())
print(datetime.datetime.now())

t0 = datetime.datetime.strptime(args[3],"%Y-%m-%d-%H:%M")
t1 = datetime.datetime.now()

print("Desde la fecha dada han pasado:")
print(t1 - t0)

url_init="https://min-api.cryptocompare.com/data/pricehistorical"
url_request = url_init + "?" + "fsym=" + args[2] + "&tsyms=" + "USD,LTC,ETH" + "&ts=" + str(int(t0.timestamp()))
print(url_request)

# esto funciona, te da la url donde aparece el precio de la moneda introducida en la fecha dada
# en cada una de las monedas destino.
