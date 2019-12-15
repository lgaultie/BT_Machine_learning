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

###############################################
			# First try below #
###############################################

# def reverse_caps(avs):
# 	str = avs
# 	new_str = []
# 	for x in range(len(str)):
# 		if str[x].isupper():
# 			new_str.append(str[x].lower())
# 		elif str[x].islower():
# 			new_str.append(str[x].upper())
# 		elif str[x] == ' ':
# 			new_str.append(' ')
# 	return new_str
#
#
# def join_avs():
# 	if (len(sys.argv) > 2):
# 		arguments = []
# 		for i in range(len(sys.argv)):
# 			if i == 0:
# 				continue
# 			arguments.append(sys.argv[i])
# 		separator = ' '
# 		return separator.join(arguments)
# 	return sys.argv[1]
#
#
# def reverse_str(avs_caps):
# 	print (''.join(reversed(avs_caps)))
#
#
# avs = join_avs()
# avs = reverse_caps(avs)
# print(''.join(reversed(avs)))
