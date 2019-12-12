from aocd import get_data
from math import gcd
from re import match

data = get_data(day=12, year=2019).splitlines()
planetPosition = [[int(i) for i in match("<x=(.*), y=(.*), z=(.*)>", line).groups()] for line in data]
planetVelocity = [[0] * 3, [0] * 3, [0] * 3, [0] * 3]
step = totalEnergy = 0

# Records the location and speed of the planets on the first step for each axis
memory = [[],[],[]]

# Records how long it takes for each axis to return to the same exact position and speed
steps = [0, 0, 0]

while 0 in steps:
	planetGravity = [[0] * 3, [0] * 3, [0] * 3, [0] * 3]
	for planet1 in range(4):
		for planet2 in range(planet1+1, 4):
			for axis in range(3):
				if planetPosition[planet1][axis] < planetPosition[planet2][axis]:
					planetGravity[planet1][axis] += 1
					planetGravity[planet2][axis] -= 1
				elif planetPosition[planet1][axis] > planetPosition[planet2][axis]:
					planetGravity[planet1][axis] -= 1
					planetGravity[planet2][axis] += 1

	for planet in range(4):
		for axis in range(3):
			planetVelocity[planet][axis] += planetGravity[planet][axis]
			planetPosition[planet][axis] += planetVelocity[planet][axis]

	for axis in range(3):
		if step == 0:
			memory[axis] = [planet[axis] for planet in planetPosition] + [planet[axis] for planet in planetVelocity]
		elif not steps[axis]:
			positionAndVelocity = [planet[axis] for planet in planetPosition] + [planet[axis] for planet in planetVelocity]
			if positionAndVelocity == memory[axis]:
				steps[axis] = step
	step += 1

	if step == 1000:
		for planet in range(4):
			potential = sum([abs(planetPosition[planet][axis]) for axis in range(3)])
			kinetic = sum([abs(planetVelocity[planet][axis]) for axis in range(3)])
			totalEnergy += potential * kinetic
		print(totalEnergy)

# Calculate Least Common Multiple of the 3 axis
lcm = steps[0]
for step in steps[1:]:
	lcm = lcm * step // gcd(lcm, step)
print(lcm)