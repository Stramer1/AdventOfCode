from aocd import get_data

data = get_data(day=21, year=2020).splitlines()
allergenIngredients = {}
foods = []

for line in data:
	ingredients, allergens = line.split(" (contains ")
	allergens = allergens[:-1].split(", ")
	foods.append([allergens, ingredients.split()])
# foods = [[['eggs', 'shellfish', ...], ['fljn', 'jcks', 'gxmptfk', 'tpjmxd', 'qdlpbt']], ...]

for allergen in set([allergen for element in foods for allergen in element[0]]):
	common = []
	for food in foods:
		if allergen in food[0]:
			common = food[1] if common == [] else list(set(common).intersection(food[1]))
	allergenIngredients[allergen] = common
# allergenIngredients = {'shellfish': ['qdlpbt', 'pmvfzk', 'tsnkknk', 'kqv'], ... }

changeMade = True
while changeMade:
	changeMade = False
	for allergen1 in allergenIngredients:
		if len(allergenIngredients[allergen1]) == 1:
			for allergen2 in allergenIngredients:
				if allergen1 != allergen2 and allergenIngredients[allergen1][0] in allergenIngredients[allergen2]:
					allergenIngredients[allergen2].remove(allergenIngredients[allergen1][0])
					changeMade = True
# allergenIngredients = {'shellfish': ['qdlpbt'], ... }

print(sum([ingredient] not in allergenIngredients.values() for ingredient in [ingredient for element in foods for ingredient in element[1]]))
print(",".join(allergenIngredients[allergen][0] for allergen in sorted(allergenIngredients.keys())))