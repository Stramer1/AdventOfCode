from aocd import get_data
from re import finditer

data = get_data(day=20, year=2020).split("\n\n")[:-1]
tiles = {}

class Tile:
	def __init__(self, number, field):
		self.number = number
		self.field = field
		self.conections = set()
		self.configuration = []
		self.x = 0
		self.y = 0
		northEdge = field[0]
		eastEdge = "".join(line[-1] for line in field)
		southEdge = field[-1]
		westEdge = "".join(line[0] for line in field)

		self.configurations = [[northEdge, eastEdge, southEdge, westEdge],
						[westEdge[::-1], northEdge, eastEdge[::-1], southEdge],
						[southEdge[::-1], westEdge[::-1], northEdge[::-1], eastEdge[::-1]],
						[eastEdge, southEdge[::-1], westEdge, northEdge[::-1]],
						[southEdge, eastEdge[::-1], northEdge, westEdge[::-1]],
						[westEdge, southEdge, eastEdge, northEdge],
						[northEdge[::-1], westEdge, southEdge[::-1], eastEdge],
						[eastEdge[::-1], northEdge[::-1], westEdge[::-1], southEdge[::-1]]]

	def changeField(self, index):
		self.configuration = self.configurations[index]

		# Flip
		if index > 3:
			self.field = self.field[::-1]

		# Rotate
		for _ in range(index%4):
			self.field = ["".join([line[index] for line in self.field][::-1]) for index in range(len(self.field))]

		# Remove edges
		self.field = [line[1:-1] for line in self.field[1:-1]]

# Create Tiles
for tile in data:
	tilesList = tile.splitlines()
	tileNumber = tilesList[0][5:-1]
	tiles[tileNumber] = Tile(tileNumber, tilesList[1:])

# Find conections
for tile1 in tiles.values():
	for configuration1 in tile1.configurations:
		for edgePosition in range(4):
			for tile2 in tiles.values():
				if tile1 != tile2:
					for configuration2 in tile2.configurations:
						if configuration1[edgePosition] == configuration2[(edgePosition+2)%4]:
							tile2.conections.add(tile1)
							tile1.conections.add(tile2)

# Multiplicate corner values
multiplication = 1
for tile in tiles.values():
	if len(tile.conections) == 2:
		multiplication *= int(tile.number)
		corner = tile
print(multiplication)

def match(tile1, tile2):
	for configurationIndex in range(8):
		for edge in range(4):
			if tile1.configuration[edge] == tile2.configurations[configurationIndex][(edge+2)%4]:
				vector = [(0, -1),(1, 0), (0, 1),(-1, 0)][edge]
				tile2.changeField(configurationIndex)
				return tile1.x + vector[0], tile1.y + vector[1]

def determineCoordinates(tile1):
	for tile2 in tile1.conections:
		if tile2 != corner and tile2.x == 0 and tile2.y == 0:
			tile2.x, tile2.y = match(tile1, tile2)
			determineCoordinates(tile2)

# Hard coded value 6
corner.changeField(6)
determineCoordinates(corner)

smallX = smallY = bigX = bigY = 0
tileCoordinates = {}
for tile in tiles.values():
	smallX, smallY = min(tile.x, smallX), min(tile.y, smallY)
	bigX, bigY = max(tile.x, bigX), max(tile.y, bigY)
	tileCoordinates[repr((tile.x, tile.y))] = tile

finalImage = []
for y in range(smallY, bigY+1):
	for line in range(len(corner.field)):
		finalImage.append("".join(tileCoordinates[repr((x, y))].field[line] for x in range(smallX, bigX+1)))

# Find number of monsters
monsters = 0
for line in range(len((finalImage))):
    ns1 = [match.start(0) for match in finditer(r"(?=#....##....##....###)", finalImage[line])]
    for n1 in ns1:
        if n1 and line > 0:
            ns2 = [match.start(0) for match in finditer(r"(?=.#..#..#..#..#..#)", finalImage[line + 1])]
            if n1 in ns2:
                if finalImage[line - 1][n1 + 18] == '#':
                    monsters += 1

print(sum(line.count("#") for line in finalImage) - 15 * monsters)