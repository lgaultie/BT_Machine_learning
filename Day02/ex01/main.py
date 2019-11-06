#!/usr/bin/env python

'''Implement the what_are_the_vars function that returns an object with the
right attributes. You will have to modify the "instance" ObjectC, NOT THE CLASS.
Have a look to getattr, setattr.'''

class ObjectC(object):
	def __init__(self):
		pass

def what_are_the_vars(*args, **kwargs):
	"""Your code"""
	obj = ObjectC()
	for i in range(len(args)):
		# creating a new attribute in the instance of obj: var_i
		setattr(obj, "var_{}".format(i), args[i])
	for x in kwargs:
		# dir() gets all attributes/methods/fields/etc of an object
		if x in dir(obj):
			return
		setattr(obj, x, kwargs[x])
	return (obj)

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
		# dir() gets all attributes/methods/fields/etc of an object
	for attr in dir(obj):
		if attr[0] != '_':
# The getattr() method returns the value of the named attribute of an object.
# class Person:
#     age = 23
#     name = "Adam"
# person = Person()
# print('The age is:', getattr(person, "age"))
# print('The age is:', person.age)
# >> The age is: 23
# >> The age is: 23
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")


if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
