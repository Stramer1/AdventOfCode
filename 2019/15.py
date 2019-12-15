from aocd import get_data
from intcode import runProgram

program = list(map(int, get_data(day=15, year=2019).split(',')))
vectors = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}

class Tile:
	def __init__(self, coordinates, depth):
		self.coordinates = coordinates
		self.borders = [0, 0, 0, 0]
		self.wall = False
		self.destination = False
		self.visited = 0
		self.depth = depth
		self.depth2 = -1

	def isDestination(self):
		self.destination = True
		self.depth2 = 0

	def getBestDirection(self):
		for index, value in enumerate(self.borders):
			if value == 0:
				return index + 1
		return self.borders.index(min([tile for tile in self.borders if not tile.wall], key=lambda x: x.visited)) + 1

	def setBorder(self, direction, value):
		if self.borders[direction - 1] == 0:
			self.borders[direction - 1] = value

nextTile = currentTile = Tile((0, 0), 0)
area = {repr((0, 0)): currentTile}

def processInput():
	global currentTile, nextTile
	direction = currentTile.getBestDirection()
	newCoordinates = (currentTile.coordinates[0] + vectors[direction][0], currentTile.coordinates[1] + vectors[direction][1])

	if repr(newCoordinates) not in area:
		nextTile = Tile(newCoordinates, currentTile.depth + 1)
		area[repr(newCoordinates)] = nextTile
	else:
		nextTile = area[repr(newCoordinates)]

	if currentTile.depth2 >= 0 and nextTile.depth2 < 0:
		nextTile.depth2 = currentTile.depth2 + 1
	elif currentTile.depth2 >= 0:
		nextTile.depth2 = min(nextTile.depth2, currentTile.depth2 + 1)

	currentTile.setBorder(direction, nextTile)
	currentTile.visited += 1
	return direction

def processOutput(result):
	global currentTile, nextTile
	if result == 0:
		nextTile.wall = True
	elif result == 1:
		currentTile = nextTile
	else:
		currentTile = nextTile
		currentTile.isDestination()

def stopingCondition():
	return any(not tile.wall and tile.depth2 == -1 for tile in area.values())

runProgram(program, processInput, processOutput, stopingCondition)

print([tile.depth for tile in area.values() if tile.destination][0])
print(max(tile.depth2 for tile in area.values()))