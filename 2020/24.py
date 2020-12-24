from aocd import get_data
from ast import literal_eval
from copy import deepcopy

data = get_data(day=24, year=2020).splitlines()
vectors = {"e": (2, 0), "ne": (1, -1), "nw": (-1, -1), "w": (-2, 0), "sw": (-1, 1), "se": (1, 1)}
floor = {}

for line in data:
	direction = ""
	currentLocation = [0, 0]
	for char in line:
		if direction + char in vectors:
			vector = vectors[direction + char]
			currentLocation[0] += vector[0]
			currentLocation[1] += vector[1]
			direction = ""
			if repr(currentLocation) not in floor:
				floor[repr(currentLocation)] = False
		else:
			direction += char

	floor[repr(currentLocation)] = not floor[repr(currentLocation)]

print(sum(value for value in floor.values()))

for day in range(101):
	print(f"Day: {day}", end='\r')
	floorCopy = deepcopy(floor)
	for tile in floor:
		x, y = literal_eval(tile) 
		adjacentCoordinates = [repr([x + vector[0], y + vector[1]]) for vector in vectors.values()]

		adjacentsTiles = []
		for coordinate in adjacentCoordinates:
			if coordinate not in floor:
				floorCopy[coordinate] = False
			else:
				adjacentsTiles.append(floor[coordinate])


		if day > 0 and floor[tile] and not (0 < adjacentsTiles.count(True) < 3):
			floorCopy[tile] = False
		elif day > 0 and (not floor[tile]) and adjacentsTiles.count(True) == 2:
			floorCopy[tile] = True

	floor = floorCopy
print(sum(value for value in floor.values()))