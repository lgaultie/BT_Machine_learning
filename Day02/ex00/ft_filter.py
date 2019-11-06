#!/usr/bin/env python

# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


# function that filters vowels
def filterVowels(alphabet):
	vowels = ['a', 'e', 'i', 'o', 'u']
	if alphabet in vowels:
		return True
	else:
		return False

def ft_filter(function_to_apply, list_of_inputs):
	results = []
	for i in list_of_inputs:
		if function_to_apply(i) == True:
			results.append(i)
	return results

filteredVowels = ft_filter(filterVowels, alphabets)
for vowel in filteredVowels:
	print(vowel)

# filter(lambda x: x>5, range(10)) <=> [x for x in range(10) if x>5]
# 	[6, 7, 8, 9]
