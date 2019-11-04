#!/usr/bin/env python

import sys

t = (19,42,21)
print ("the", len(t), "numbers are: ", end = '')
for x in range(len(t)):
	if x == len(t) - 1:
		print(t[x])
	else:
		sys.stdout.write(str(t[x]))
		sys.stdout.write(", ")
