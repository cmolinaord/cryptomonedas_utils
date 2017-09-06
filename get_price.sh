#!/bin/bash

WEB_ROOT="https://api.coinmarketcap.com/v1/ticker"
COIN=$1
TIME=$2
if [[ $TIME == "1h" || $TIME == "24h" || $TIME == "7d" ]]
then
	CHANGE_STRING=`echo "percent_change_$TIME"`
elif [[ $TIME == "" ]]
then
	CHANGE_STRING=""
else
	echo "   ***Error: TIME must be '1h', '24h' or '7d'"
	exit
fi

if [[ $3 == '--no-color' ]]
then
	unset RED
	unset GREEN
	unset NC
else
	RED='\033[1;31m'
	GREEN='\033[1;32m'
	NC='\033[0m'
fi

if [[ $COIN == "" ]]
then
	echo "   ***Error: Dime una moneda por favor"
else
	content=$(curl -s "$WEB_ROOT/$COIN/")
	symbol=$(echo $content | sed "s/,/\n/g" | grep "symbol" | cut -d'"' -f4)
	price_usd=$(echo $content | sed "s/,/\n/g" | grep "price_usd" | cut -d'"' -f4)
	if [[ $CHANGE_STRING != "" ]]
	then
		change=$(echo $content | sed "s/,/\n/g" | grep $CHANGE_STRING | cut -d'"' -f4)
		if [[ $CHANGE == "-*" ]]
		then
			echo -e "1$symbol = $price_usd USD ($TIME: $RED$change%$NC)"
		else
			echo -e "1$symbol = $price_usd USD ($TIME: $GREEN$change%$NC)"
		fi
	else
		if [[ $CHANGE == "-*" ]]
		then
			echo -e "1$symbol = $price_usd USD"
		else
			echo -e "1$symbol = $price_usd USD"
		fi
	fi
fi
