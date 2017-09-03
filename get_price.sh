#!/bin/bash

WEB_ROOT="https://api.coinmarketcap.com/v1/ticker"
COIN=$1

if [[ $1 == "" ]]
then
	echo "Dime una moneda por favor"
else
	content=$(curl -s "$WEB_ROOT/$COIN/")
	symbol=$(echo $content | sed "s/,/\n/g" | grep "symbol" | cut -d'"' -f4)
	price_usd=$(echo $content | sed "s/,/\n/g" | grep "price_usd" | cut -d'"' -f4)
	echo "1 $symbol = $price_usd USD"
fi
