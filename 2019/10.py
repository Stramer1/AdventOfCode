from aocd import get_data
import numpy as np

data = get_data(day=10, year=2019).splitlines()
width, height = len(data[0]), len(data)
asteroids = [(x, y) for y in range(height) for x in range(width) if data[y][x] == "#"]
asteroidsInSight = [0]*len(asteroids)

def angleBetween(a, b):
	angle = np.rad2deg(np.arctan2(np.cross(a,b), np.dot(a,b)))
	return angle + 360 if angle < 0 else angle

def canSeeEachOther(asteroid1, asteroid2):
	vector = np.subtract(asteroid1, asteroid2)
	divisor = np.gcd(vector[0], vector[1])
	vector = vector//divisor
	position = np.sum([asteroid2, vector], axis=0)
	
	while not np.array_equal(asteroid1, position):
		if data[position[1]][position[0]] == "#":
			return False
		position = np.sum([position, vector], axis=0)
	return True


def asteroidsInBetween(center, asteroid):
	vector = np.subtract(center, asteroid)
	divisor = np.gcd(vector[0], vector[1])
	vector = vector//divisor
	position = np.sum([asteroid, vector], axis=0)
	order = 0
	
	while not np.array_equal(center, position):
		if data[position[1]][position[0]] == "#":
			order += 1
		position = np.sum([position, vector], axis=0)
	return order

for asteroid1 in range(len(asteroids)):
	for asteroid2 in range(asteroid1 + 1, len(asteroids)):
		if canSeeEachOther(asteroids[asteroid1], asteroids[asteroid2]):
			asteroidsInSight[asteroid1] += 1
			asteroidsInSight[asteroid2] += 1

maximum = max(asteroidsInSight)
center = asteroids[asteroidsInSight.index(maximum)]
asteroids.remove(center)
orderedAsteroids = sorted([(asteroidsInBetween(center, asteroid), angleBetween((0, -1), np.subtract(asteroid, center)), asteroid) for asteroid in asteroids])

print(maximum)
print(orderedAsteroids[199][2][0] * 100 + orderedAsteroids[199][2][1])