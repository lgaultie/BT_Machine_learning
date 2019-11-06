#!/usr/bin/env python

def addition(n):
	return n + n


def ft_map(function_to_apply, list_of_inputs):
	result = []
	for i in list_of_inputs:
		result.append(function_to_apply(i))
	return result


numbers = [1, 2, 3, 4]
res = ft_map(addition, numbers)
print (res)

chars = ['s', 'k', 'k', 'a', 'v']
converted = list(ft_map(lambda s: str(s).upper(), chars))
print(converted)
