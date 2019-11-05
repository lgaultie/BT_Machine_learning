#!/usr/bin/env python

class Book:
	def __init__(self, name=None, last_update=0, creation_date=0,
				recipes_list={"starter": {}, "lunch": {}, "dessert": {}}):
		self.name = name
		self.last_update = last_update
		self.creation_date = creation_date
		self.recipes_list =	recipes_list


	def get_recipes_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		for j in self.recipes_list:
			for i in self.recipes_list[j]:
				if i == name:
					to_print = str(self.recipes_list[j][i])
					print(to_print)


	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		for i in self.recipes_list[recipe_type]:
			print("{} ".format(self.recipes_list[recipe_type][i]["name"]))


	def add_recipe(self, recipe):
		""" Add a recipe to the book and update last_update """
		new_dic = {"name": recipe.name, "cooking_lvl":recipe.cooking_lvl,
				"cooking_time": recipe.cooking_time, "ingredients":recipe.ingredients,
				"description": recipe.description, "recipe_type": recipe.recipe_type}
		self.recipes_list[recipe.recipe_type][recipe.name] = new_dic
		print(self.recipes_list[recipe.recipe_type])
