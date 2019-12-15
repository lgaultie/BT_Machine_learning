#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
	print("ERROR")
	exit()
argv = sys.argv[1]
try:
	nb = int(argv)
except ValueError:
	print("ERROR")
	exit()
if (nb == 0):
	print("I'm Zero.")
elif (nb % 2 == 0):
	print("I'm even.")
elif not (nb % 2 == 0):
	print("I'm odd.")
