#!/usr/bin/env python

class Recipe:
	""" Contains informations about a recipe"""
	def __init__(self, name="None", cooking_lvl=0, cooking_time=0,
				ingredients=["??", "??"], description=None, recipe_type=None):
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = ("Name : {}\nCooking level: {}\nTime to cook: {}\nIngredients: {}\nDescription: {}\nRecipe type: {}\n--------"
				.format(self.name, self.cooking_lvl, self.cooking_time,
				', '.join(self.ingredients), self.description, self.recipe_type))
		return txt
