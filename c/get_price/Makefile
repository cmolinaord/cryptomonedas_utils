CFLAGS = -Wall -Werror
.PHONY : all

all: get_price

get_price: get_price.c
	gcc -lcurl get_price.c -o get_price

clean:
	rm -v *.o get_price
