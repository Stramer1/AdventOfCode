from aocd import get_data

data = get_data(day=3, year=2019).splitlines()

def calculatePath(directions):
	path = []
	location = [0, 0]
	for direction in directions:
		for i in range(int(direction[1:])):
			if direction[0] == "R":
				location[0] += 1
			elif direction[0] == "L":
				location[0] -= 1
			elif direction[0] == "U":
				location[1] += 1
			elif direction[0] == "D":
				location[1] -= 1
			path.append(tuple(location))
	return path

wirePath1 = calculatePath(data[0].split(","))
wirePath2 = calculatePath(data[1].split(","))
intersections = set(wirePath1).intersection(wirePath2)

print(min(map(lambda e : abs(e[0]) + abs(e[1]), intersections)))
print(min(map(lambda e : 2 + wirePath1.index(e) + wirePath2.index(e), intersections)))