from aocd import get_data

data = get_data(day=3, year=2020).splitlines()
height, width = len(data), len(data[0])

def findTrees(slopeX, slopeY):
	trees = currentX = currentY = 0

	while currentY < height:
		if data[currentY][currentX] == "#":
			trees += 1
		currentY += slopeY
		currentX = (currentX + slopeX) % width
	return trees

print(findTrees(3, 1))
print(findTrees(1, 1) * findTrees(3, 1) * findTrees(5, 1) * findTrees(7, 1) * findTrees(1, 2))