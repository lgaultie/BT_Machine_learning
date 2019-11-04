#!/usr/bin/env python

import sys

def check_avs():
	if len(sys.argv) > 3 or len(sys.argv) < 3:
		print ("ERROR")
		exit()
	if isinstance(sys.argv[1], str) == True:
		for x in sys.argv[1]:
			if not x.isalpha() and not x.isspace():
				print("ERROR")
				exit()
	if sys.argv[2].isdigit() == False:
		print("ERROR")
		exit()


def create_list():
	list = []
	list = sys.argv[1].split()
	return (list)


def modify_list(list):
	for elem in list:
		if len(elem) <= int(sys.argv[2]):
			list.remove(elem)
	print (list)

check_avs()
list = create_list()
modify_list(list)
