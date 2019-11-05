#!/usr/bin/env python

from book import Book
from recipe import Recipe
import datetime

# def print_cake():
# 	""" create and print a cake recipe, checks if it works with empty recipes """
# 	empty_recipe = Recipe()
# 	to_print2 = str(empty_recipe)
# 	print ("test: printing empty recipe")
# 	print(to_print2)
# 	ingredients = ["chocolate", "flour", "sugar"]
# 	cake = Recipe("Cake", 2, 11, ingredients, "it's good", "dessert")
# 	to_print = str(cake)
# 	print ("test: printing new recipe")
# 	print(to_print)


def add_cake():
	""" create and print a cake recipe, checks if it works with empty recipes """

	ingredients = ["chocolate", "flour", "sugar"]
	cake = Recipe("Cake", 2, 11, ingredients, "it's good", "dessert")
	new_dic = {"name": cake.name, "cooking_lvl":cake.cooking_lvl,
			"cooking_time": cake.cooking_time, "ingredients":cake.ingredients,
			"description": cake.description, "recipe_type": cake.recipe_type}

	ingredients = ["ice", "cream", "sugar"]
	icecream = Recipe("Ice-cream", 8, 11, ingredients, "it's good", "dessert")
	new_dic2 = {"name": icecream.name, "cooking_lvl":icecream.cooking_lvl,
			"cooking_time": icecream.cooking_time, "ingredients":icecream.ingredients,
			"description": icecream.description, "recipe_type": icecream.recipe_type}

	ingredients = ["vegetable", "cream"]
	soup = Recipe("Soup", 4, 15, ingredients, "it's good", "starter")
	new_dic3 = {"name": soup.name, "cooking_lvl": soup.cooking_lvl,
			"cooking_time": soup.cooking_time, "ingredients":soup.ingredients,
			"description": soup.description, "recipe_type": soup.recipe_type}

	ingredients = ["eggs", "salt"]
	omelet = Recipe("Omelet", 1, 5, ingredients, "it's good", "lunch")
	new_dic4 = {"name": omelet.name, "cooking_lvl":omelet.cooking_lvl,
			"cooking_time": omelet.cooking_time, "ingredients":omelet.ingredients,
			"description": omelet.description, "recipe_type": omelet.recipe_type}
	book = Book("Cookbook", datetime.datetime.today(), datetime.datetime.today())
	# [cake.name] name of new entry
	book.recipes_list[cake.recipe_type][cake.name] = new_dic
	book.recipes_list[icecream.recipe_type][icecream.name] = new_dic2
	book.recipes_list[soup.recipe_type][soup.name] = new_dic3
	book.recipes_list[omelet.recipe_type][omelet.name] = new_dic4
	return book


def choose(book, str):
	if str == "1":
		name = input("Name: ")
		lvl = input("Level: ")
		time = input("Time to make: ")
		ingredient = input("Ingredients: ")
		description = input("Description: ")
		type = input("Type (starter, lunch, dessert): ")
		if not type == "starter" and not type == "lunch" and not type == "dessert":
			print ("The recipe type must be starter, lunch, or dessert.")
			exit()
		new = Recipe(name, lvl, time, ingredient, description, type)
		book.add_recipe(new)
		choose(book, input("Hi ! What do you want to do?\n1/ Add a recipe\n2/ Get recipes by names\n3/ Get recipes by types\n4/ Exit\n"))
	elif str == "2":
		name = input("Name of the recipe you are looking for: ")
		book.get_recipes_by_name(name)
	elif str == "3":
		type = input("Type (starter, lunch, dessert): ")
		if not type == "starter" and not type == "lunch" and not type == "dessert":
			print ("The recipe type must be starter, lunch, or dessert.")
			exit()
		book.get_recipes_by_types(type)
	elif str == "4":
		exit()
	else:
		choose(book, input("You failed...\n1/ Add a recipe\n2/ Get recipes by names\n3/ Get recipes by types\n4/ Exit\n"))


# print_cake()
book = add_cake()
print("Actual recipes in the book:")
for i in book.recipes_list:
	for j in book.recipes_list[i]:
		print("{} ".format(book.recipes_list[i][j]["name"]))

choose(book, input("---\nHi ! What do you want to do?\n1/ Add a recipe\n2/ Get recipes by names\n3/ Get recipes by types\n4/ Exit\n"))
