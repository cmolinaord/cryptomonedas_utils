.PHONY: install

install:
	install -Dm755 ./get_price.sh /usr/bin/crypto_getprice

uninstall: rm -f /usr/bin/crypto_getprice
