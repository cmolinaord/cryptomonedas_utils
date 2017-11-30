.PHONY: install

install:
	pip install engineering_notation
	install -Dm755 ./get_prices.py /usr/bin/crypto_getprice

uninstall: rm -f /usr/bin/crypto_getprice
