#!/usr/bin/env python

cookbook = {
			"sandwich": {"ingredients": ["ham", "bread", "cheese", "tomatoes"],
						"meal": "lunch",
						"prep_time": 10},
			"cake": {"ingredients": ["flour", "sugar", "eggs"],
					"meal": 'dessert',
					"prep_time": 60},
			"salad": {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
					"meal": "lunch",
					"prep_time": 15}
			}


def print_cookbook():
	for x in cookbook:
		print("A", x, "is made of:", end='')
		for i in cookbook[x]['ingredients']:
			print(" %s" % i, end='')
		print(". It's a",cookbook[x]['meal'], end='')
		print(" and it takes",cookbook[x]['prep_time'],"mins to make.")


def print_recipes(ret):
	print("Ingredients list: ", cookbook[ret]['ingredients'])


def delete_recipes(ret):
	del(cookbook[ret])
	print(ret, "has been deleted")


def add_recipe(name, ingredients, meal, prep):
	cookbook.update({name : {"ingredients": ingredients, "meal": meal, "prep_time": prep}})
	print("recipe", name, "has beed added.")


def choose(str):
	if str == "1":
		name = input("Name of recipe:\n>> ")
		ingredients = input("ingredients\n>> ")
		meal = input("Kind of meal:\n>> ")
		prep = input("How long to make (in mins):\n>> ")
		add_recipe(name, ingredients, meal, prep)
	elif str == "2":
		ret = input("Please enter the recipe's name you want to delete:\n>> ")
		delete_recipes(ret)
	elif str == "3":
		ret = input("Please enter the recipe's name to get its details:\n>> ")
		print_recipes(ret)
	elif str == "4":
		print_cookbook()
	elif str == "5":
		print ("Cookbook closed.")
		exit ()
	else:
		choose(input("This option does not exist, pleace type the corresponding number.\nTo exit, enter 5.\n>> "))
	choose(input("\nPlease select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>> "))


choose(input("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>> "))
