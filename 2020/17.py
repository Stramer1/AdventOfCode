from aocd import get_data
from copy import deepcopy
from itertools import product

data = list(map(list, get_data(day=17, year=2020).splitlines()))
ACTIVE, INACTIVE = "#", "."
size = len(data)
vectors = list(product([1, 0, -1], repeat=4))
vectors.remove((0, 0, 0, 0))
space = {repr((x-(size//2), y-(size//2), 0, 0)): data[y][x] for x in range(size) for y in range(size)}
spaceCopy = deepcopy(space)

def calcSurroundings(x, y, z, w):
	surroundings = []
	for vector in vectors:
		surrounding = repr((x + vector[0], y + vector[1], z + vector[2], w + vector[3]))
		if surrounding not in space:
			space[surrounding] = INACTIVE
		surroundings.append(space[surrounding])
	return surroundings

for step in range(6):
	size +=2
	for w in range(-(size//2), size//2+1):
		for z in range(-(size//2), size//2+1):
			for y in range(-(size//2), size//2+1):
				for x in range(-(size//2), size//2+1):
					cube = repr((x, y, z, w))
					if cube not in space:
						space[cube] = INACTIVE
					surroundings = calcSurroundings(x, y, z, w)
					if space[cube] == ACTIVE and surroundings.count(ACTIVE) not in [2, 3]:
						spaceCopy[cube] = INACTIVE
					elif space[cube] == INACTIVE and surroundings.count(ACTIVE) == 3:
						spaceCopy[cube] = ACTIVE
	space = deepcopy(spaceCopy)
print(list(space.values()).count(ACTIVE))