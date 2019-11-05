#!/usr/bin/env python

import secrets

def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''
	if option == None:
		line_split = txt.split(sep)
		print("\n".join(line_split))

	elif option == "ordered":
		line_split = txt.split(sep)
		line_split.sort()
		print("\n".join(line_split))

	elif option == "shuffle":
		line_split = txt.split(sep)
		length = len(line_split)
		list_index = []
		length2 = len(list_index)
		while length2 is not length:
			for i in range(length):
				#generates random int between 0 and length
				nb = secrets.randbelow(length)
				if nb in list_index:
					continue
				else:
					list_index.append(nb)
				length2 = len(list_index)
		for x in range(length2):
			print(line_split[list_index[x]])

	else:
		print("ERROR - option not found.")
		exit()

txt = "Hi how are you"
sep = ' '
print("---- Original text ----")
generator(txt, sep)
print("---- Shuffled text ----")
generator(txt, sep, "shuffle")
print("---- Ordered text ----")
generator(txt, sep, "ordered")
