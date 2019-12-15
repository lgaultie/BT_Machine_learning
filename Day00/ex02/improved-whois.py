#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
	sys.exit("ERROR")
argv = sys.argv[1]
try:
	nb = int(argv)
except ValueError:
	sys.exit("ERROR")
if (nb == 0):
	print("I'm Zero.")
elif (nb % 2 == 0):
	print("I'm even.")
elif not (nb % 2 == 0):
	print("I'm odd.")
