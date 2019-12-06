from aocd import get_data

data = list(map(lambda e : e.split(")"), get_data(day=6, year=2019).splitlines()))
dic = {"COM": 0}

for pair in data:
	dic[pair[1]] = pair[0]

planet = "YOU"
visited = []
while planet != "COM":
	planet = dic[planet]
	visited.append(planet)

planet = "SAN"
total = 0
while dic[planet] not in visited:
	planet = dic[planet]
	total +=1

total += visited.index(dic[planet])

def calculateOrbit(planet):
	if type(dic[planet]) == int:
		return dic[planet]
	else:
		orbits = 1 + calculateOrbit(dic[planet])
		dic[planet] = orbits
		return orbits

print(sum([calculateOrbit(planet) for planet in dic]))
print(total)