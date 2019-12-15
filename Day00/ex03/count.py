#!/usr/bin/env python

import sys
import string


def count_things(str):
	upper = 0
	total = 0
	lower = 0
	space = 0
	punc = 0
	for x in str:
		total += 1
		if x.isupper():
			upper += 1
		elif x.islower():
			lower += 1
		elif x == ' ':
			space += 1
		elif x in string.punctuation:
			punc += 1
	print("the text contains", total, "characters:")
	print("-", upper, "upper letters")
	print("-", lower, "lower letters")
	print("-", punc, "punctuation marks")
	print("-", space, "spaces")


def text_analyzer(str = 0):
	"""This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text."""
	if str is 0:
		count_things(input("What is the text to analyse ?\n>>"))
	else:
		count_things(str)
