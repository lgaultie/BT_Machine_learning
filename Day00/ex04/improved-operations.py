#!/usr/bin/env python

import sys

def check_avs(length):
	if length < 2 or length > 3:
		if length > 3:
			print("InputError: too many arguments")
		sys.exit("Usage: python operations.py\nExample:\n	python operations.py 10 3")


def calculate():
	try:
		nb0 = int(sys.argv[1])
		nb1 = int(sys.argv[2])
	except ValueError:
		sys.exit("InputError: only numbers\nUsage: python operations.py\nExample:\n	python operations.py 10 3")
	print("Sum:		", nb0 + nb1)
	print("Difference:	", nb0 - nb1)
	print("Product:	", nb0 * nb1)
	if (nb1 == 0):
		print("Quotient:	ERROR (div by zero)")
	else:
		print("Quotient:	", nb0 / nb1)
	if (nb1 == 0):
		print("Quotient:	ERROR (modulo by zero)")
	else:
		print("Remainder:	", nb0 % nb1)

length = len(sys.argv)
check_avs(length)
calculate()
