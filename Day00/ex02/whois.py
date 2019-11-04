#!/usr/bin/env python

import sys

def whois(nb):
	if nb == 0:
		print ("I'm Zero.")
	elif nb % 2 == 0:
		print ("I'm even.")
	else:
		print ("I'm odd.")

def check_avs():
	if len(sys.argv) > 2:
		print ("ERROR")
		exit()
	for x, argv in enumerate(sys.argv):
		if x == 0 or sys.argv[x].isnumeric() == True:
			continue
		else:
			print ("ERROR")
			exit()
	nb = int(sys.argv[1])
	return (nb)

nb = check_avs()
whois(nb)
