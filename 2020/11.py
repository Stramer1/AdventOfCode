from aocd import get_data
from copy import deepcopy

data = list(map(list, (day=11, year=2020).splitlines()))
dataCopy = deepcopy(data)
vectors = ((0,1), (0,-1), (1,-1), (1,0), (1,1), (-1,-1), (-1,0), (-1,1))

# Part 1
def calcSurroundings1(line, seat):
	surroundings = []
	for vector in vectors:
		if -1 < line + vector[0] < len(data) and -1 < seat + vector[1] < len(data[line]):
			surroundings.append(data[line+vector[0]][seat+vector[1]])
	return surroundings

# Part 2
def calcSurroundings2(y, x):
	surroundings = []
	for vector in vectors:
		found = False
		multiplier = 1
		while not found:
			surroundingX = x + multiplier * vector[1]
			surroundingY = y + multiplier * vector[0]

			if -1 < surroundingY < len(data) and -1 < surroundingX < len(data[y]):
				if data[surroundingY][surroundingX] != ".":
					surroundings.append(data[surroundingY][surroundingX])
					found = True
				else:
					multiplier += 1
			else:
				found = True
	return surroundings

changeMade = True
while changeMade:
	changeMade = False
	for line in range(len(data)):
		for seat in range(len(data[line])):
			surroundings = calcSurroundings2(line, seat)
			if data[line][seat] == "L" and "#" not in surroundings:
				dataCopy[line][seat] = "#"
				changeMade = True
			elif data[line][seat] == "#" and surroundings.count("#") >= 5:
				dataCopy[line][seat] = "L"
				changeMade = True
	data = deepcopy(dataCopy)

print(sum(line.count("#") for line in data))