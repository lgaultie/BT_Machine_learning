#!/usr/bin/env python

import sys


def reverse_caps(avs):
	str = avs
	new_str = []
	for x in range(len(str)):
		if str[x].isupper():
			new_str.append(str[x].lower())
		elif str[x].islower():
			new_str.append(str[x].upper())
		elif str[x] == ' ':
			new_str.append(' ')
	return new_str


def join_avs():
	if (len(sys.argv) > 2):
		arguments = []
		for i in range(len(sys.argv)):
			if i == 0:
				continue
			arguments.append(sys.argv[i])
		separator = ' '
		return separator.join(arguments)
	return sys.argv[1]


def reverse_str(avs_caps):
	print (''.join(reversed(avs_caps)))


avs = join_avs()
avs = reverse_caps(avs)
print(''.join(reversed(avs)))
