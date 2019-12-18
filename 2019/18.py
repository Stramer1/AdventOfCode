from aocd import get_data

data = get_data(day=18, year=2019).splitlines()
vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
graph, adjacencyMatrix = {}, {}
keyList =  []
startingPoints = []

# Only for part 2, comment for part 1
def changeData(data):
	for y in range(1, len(data) - 1):
		for x in range(1, len(data[0]) - 1):
			if data[y][x] == "@":
				data[y - 1] = data[y - 1][:x - 1] + "@#@" + data[y - 1][x + 2:]
				data[y] = data[y][:x - 1] + "###" + data[y][x + 2:]
				data[y + 1] = data[y + 1][:x - 1] + "@#@" + data[y + 1][x + 2:]
				return data
data = changeData(data)


class Node:
	def __init__(self, coordinates):
		self.coordinates = coordinates
		self.neighbours = []
		self.wasVisited = False
		self.distance = self.doorsRequired = self.door = self.key = 0

class Path:
	def __init__(self, locations, keys, distance, maxKeys):
		self.locations = locations
		self.maxKeys = maxKeys
		self.keys = keys
		self.distance = distance

	def __repr__(self):
		return repr(self.locations) + repr(self.keys)

	def isCompleted(self):
		return self.keys == self.maxKeys

def keyIsNotInPossession(keys, key):
	return int(str(keys), 2) & int(str(key), 2) == 0

def keysUnlockDoors(keys, doors):
	return int(str(doors), 2) & int(str(keys), 2) == int(str(doors), 2)


# Create a graph as an adjacency list where 1 coordinate is 1 node
for y in range(1, len(data) - 1):
	for x in range(1, len(data[0]) - 1):
		if data[y][x] != "#":
			node = Node((x, y))
			graph[repr((x, y))] = node

			if data[y][x] == "@":
				startingPoints.append(node)
			elif data[y][x].islower():
				node.key = data[y][x]
				keyList.append(node)
			elif data[y][x] != ".":
				node.door = data[y][x]

			for v in vectors:
				x1, y1 = x + v[0], y + v[1]
				if data[y1][x1] != "#" and repr((x1, y1)) in graph:
					node.neighbours.append(graph[repr((x1, y1))])
					graph[repr((x1, y1))].neighbours.append(node)

# Convert door and key char (a, A) to 10 ** index of the key in keyList, to allow "binary" operations
for node in graph.values():
	if node.door:
		node.door = 10 ** next(i for i, v in enumerate(keyList) if node.door.lower() == v.key)

for i, node in enumerate(keyList):
	node.key = 10 ** i

# Create a weighted graph as an adjacencyMatrix where 1 node is 1 key (plus the starting positions)
# Weights are the distance + the doors between any two keys
for key1 in keyList + startingPoints:
	adjacencyMatrix[key1] = {}

	for key2 in keyList:
		adjacencyMatrix[key1][key2] = [-1, float("inf")]

	toVisit = [key1]

	while toVisit != []:
		node = toVisit.pop(0)
		node.wasVisited = True

		if node.door and int(str(node.doorsRequired), 2) & int(str(node.door), 2) == 0:
			node.doorsRequired += node.door
		
		for neighbour in node.neighbours:
			if not neighbour.wasVisited:
				toVisit.append(neighbour)
				neighbour.distance = node.distance + 1
				neighbour.doorsRequired = node.doorsRequired

		if node.key:
			adjacencyMatrix[key1][node][0] = node.doorsRequired
			adjacencyMatrix[key1][node][1] = node.distance

	for node in graph.values():
		node.distance = node.doorsRequired = 0
		node.wasVisited = False

# Part 1
# Recursively search for the shortest path as a DFS taking into account the doors
def visit(point, keys, cache):
	if repr(point) + repr(keys) in cache:
		return cache[repr(point) + repr(keys)]

	minimum = 0
	for destiny in adjacencyMatrix[point]:
		if destiny != point and keyIsNotInPossession(keys, destiny.key) and keysUnlockDoors(keys, adjacencyMatrix[point][destiny][0]):
			result = visit(destiny, keys + destiny.key, cache) + adjacencyMatrix[point][destiny][1]
			minimum = result if minimum == 0 else min(minimum, result)
	cache[repr(point) + repr(keys)] = minimum
	return minimum

print(visit(startingPoints[0], 0, {}))

# Part 2
# Basically the same as the above without recursion
maxKeys = sum(10**i for i in range(len(keyList)))
paths = [Path(startingPoints, 0, 0, maxKeys)]
cache = {}
minimumDistance = float("inf")

while paths != []:
	path = paths.pop(-1)
	print(minimumDistance, len(paths), "    ", end="\r")

	if path.isCompleted():
		minimumDistance = min(path.distance, minimumDistance)
	elif path.distance >= minimumDistance:
		continue
	elif repr(path) not in cache or cache[repr(path)] > path.distance:
		cache[repr(path)] = path.distance

		for i in range(4):
			for destiny in adjacencyMatrix[path.locations[i]]:
				if destiny != path.locations[i] and \
					keyIsNotInPossession(path.keys, destiny.key) and \
					keysUnlockDoors(path.keys, adjacencyMatrix[path.locations[i]][destiny][0]):
					paths.append(Path(path.locations[:i] + [destiny] + path.locations[i+1:],
						path.keys + destiny.key,
						path.distance + adjacencyMatrix[path.locations[i]][destiny][1], maxKeys))

print(minimumDistance)