#!/usr/bin/env python

import sys

phrase = "The right format"
length = len(phrase)

for x in range(0,42-length):
	sys.stdout.write("-")
sys.stdout.write(phrase)
