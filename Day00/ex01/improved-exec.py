#!/usr/bin/env python

import sys

# slice: [x:y:z] x index start, y index end, z = -1 move one step backward
str = [' '.join(sys.argv[1:])];
for word in str:
	for letter in word[::-1]:
		if letter.isspace():
			print(' ', end = '')
		elif letter.isupper():
			print(letter.lower(), end = '')
		elif letter.islower():
			print(letter.upper(), end = '')
print()
