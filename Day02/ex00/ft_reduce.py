#!/usr/bin/env python

from functools import reduce

def afficher(a, b):
	print("Entrée :", a, b)
	print("Sortie :", a + b)
	return a + b

def ft_reduce(function_to_apply, list_of_inputs):
	'''
    Initially, the function is called with the first two items from the
	sequence and the result is returned. The function is then called again
	with the result obtained in step 1 and the next value in the sequence.
	This process keeps repeating until there are items in the sequence.'''
	first = list_of_inputs[0]
# >>> word[:2]   # character from the beginning to position 2 (excluded)
# >>> word[4:]   # characters from position 4 (included) to the end
	for i in list_of_inputs[1:]:
		first = function_to_apply(first, i)
	return first


res = ft_reduce(afficher, range(10))
print("Résultat final", res)
