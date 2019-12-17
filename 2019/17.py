from aocd import get_data
from intcode import runProgram

program = list(map(int, get_data(day=17, year=2019).split(',')))
inputIndex = dust = alignmentTotal = facingDirection = 0
vectors = [(0, -1), (1, 0), (0, 1), (-1, 0)]
area = ""
path = []

def processInput():
	global inputIndex
	value = inputList[inputIndex]
	inputIndex += 1
	return value

def processOutput(output):
	global area, dust
	dust = output
	area += chr(output)

runProgram(program, processInput, processOutput)

# Calculate alignement total and current location
area = area.split("\n")[:-2]
for y in range(1, len(area) - 1):
	for x in range(1, len(area[0]) - 1):
		if area[y][x] == area[y + 1][x] == area[y - 1][x] == area[y][x + 1] == area[y][x - 1] == "#":
			alignmentTotal += x * y
		elif area[y][x] == "^":
			currentLocation = (x, y)

print(alignmentTotal)

def pathAhead(currentLocation, direction):
	y = currentLocation[1] + vectors[direction][1]
	x = currentLocation[0] + vectors[direction][0]
	return -1 < x < len(area[0]) and -1 < y < len(area) and area[y][x] == "#"

# Construct the path list by going through the # path
while True:
	if pathAhead(currentLocation, facingDirection):
		if len(path) > 0 and isinstance(path[-1], int):
			path[-1] += 1
		else:
			path.append(1)
		currentLocation = (currentLocation[0] + vectors[facingDirection][0], currentLocation[1] + vectors[facingDirection][1])
	elif pathAhead(currentLocation, (facingDirection + 1) % 4):
		facingDirection = (facingDirection + 1) % 4
		path.append("R")
	elif pathAhead(currentLocation, (facingDirection - 1) % 4):
		facingDirection = (facingDirection - 1) % 4
		path.append("L")
	else:
		break

# Brute force dividing the path into 3 repeatable sections
def calculate():
	for A1 in range(2, 12, 2):
		for B0 in range(A1, len(path) - 4, 2):
			for B1 in range(B0 + 2, B0 + 10, 2):
				for C0 in range(B1, len(path) - 2, 2):
					for C1 in range(C0 + 2, C0 + 10, 2):
						pathWithoutA = repr(path).replace(repr(path[:A1])[1:-1], "A")
						pathWithoutAB = pathWithoutA.replace(repr(path[B0:B1])[1:-1], "B")
						pathWithoutABC = pathWithoutAB.replace(repr(path[C0:C1])[1:-1], "C")

						if all(i in "ABC, " for i in pathWithoutABC[1:-1]):
							return pathWithoutABC[1:-1], path[:A1], path[B0:B1], path[C0:C1]

main, A, B, C = calculate()
main = [ord(x) for x in main.replace(" ", "")] + [ord("\n")]
A = [ord(x) for x in ",".join(str(i) for i in A)] + [ord("\n")]
B = [ord(x) for x in ",".join(str(i) for i in B)] + [ord("\n")]
C = [ord(x) for x in ",".join(str(i) for i in C)] + [ord("\n"), ord("n"), ord("\n")]
inputList = main + A + B + C

program[0] = 2
runProgram(program, processInput, processOutput)
print(dust)