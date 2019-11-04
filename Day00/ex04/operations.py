#!/usr/bin/env python

import sys

def check_avs():
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		if len(sys.argv) > 3:
			print("InputError: too many arguments")
		print("Usage: python operations.py")
		print("Example:")
		print("	python operations.py 10 3")
		exit()
	for x in range(len(sys.argv)):
		if x == 0:
			continue
		if not sys.argv[x].isnumeric():
			print("InputError: only numbers")
			print("Usage: python operations.py")
			print("Example:")
			print("	python operations.py 10 3")
			exit()


def calculate():
	nb0 = int(sys.argv[1])
	nb1 = int(sys.argv[2])
	print("Sum:		", nb0+nb1)
	print("Difference:	", nb0-nb1)
	print("Product:	", nb0*nb1)
	if (nb1 == 0):
		print("Quotient:	ERROR (div by zero)")
	else:
		print("Quotient:	", nb0/nb1)
	if (nb1 == 0):
		print("Quotient:	ERROR (modulo by zero)")
	else:
		print("Remainder:	", nb0%nb1)

check_avs()
calculate()
