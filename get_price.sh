#!/bin/bash

WEB_ROOT="https://api.coinmarketcap.com/v1/ticker"
COIN=$1

if [[ $2 == '--no-color' ]]
then
	unset RED
	unset GREEN
	unset NC
else
	RED='\033[1;31m'
	GREEN='\033[1;32m'
	NC='\033[0m'
fi

if [[ $1 == "" ]]
then
	echo "Dime una moneda por favor"
else
	content=$(curl -s "$WEB_ROOT/$COIN/")
	symbol=$(echo $content | sed "s/,/\n/g" | grep "symbol" | cut -d'"' -f4)
	price_usd=$(echo $content | sed "s/,/\n/g" | grep "price_usd" | cut -d'"' -f4)
	change_1h=$(echo $content | sed "s/,/\n/g" | grep "percent_change_1h" | cut -d'"' -f4)
	if [[ $change_1h == "-*" ]]
	then
		echo -e "1$symbol = $price_usd USD (1h: $RED$change_1h%$NC)"
	else
		echo -e "1$symbol = $price_usd USD (1h: $GREEN$change_1h%$NC)"
	fi
fi
