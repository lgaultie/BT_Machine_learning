#!/usr/bin/env python

import time
from random import randint
from functools import wraps

def timing(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = f(*args, **kwargs)
		end = time.time()
		print ("Elapsed time: {}".format(end-start))
		return result
	return wrapper

@timing
def log(fun):
	log = open("machine.log", 'a')
	log.write("(lgaultie)Running: %s"%fun.__name__)
	log.write("			[exec-time = ]\n")
	return (fun)

class CoffeeMachine():
	water_level = 100
	# The @log will write info about the decorated function in a machine.log file.
	@log
	# start_machine = log(start_machine)
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1,5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)
