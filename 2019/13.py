from aocd import get_data
from intcode import runProgram

program = list(map(int, get_data(day=13, year=2019).split(',')))
character = {0: " ", 1: "#", 2: "+", 3: "^", 4: "o"}
barX = ballX = 0
screen, outputs = [], []
program[0] = 2

def addPixel(x, y, value):
	global screen, ballX, barX
	if y >= len(screen):
		screen += [[" "]] * (y - len(screen) + 1) 
	if x >= len(screen[y]):
		screen[y] += [" "] * (x - len(screen[y]) + 1)
	screen[y][x] = character[value]
	if value == 4:
		ballX = x
	elif value == 3:
		barX = x

def processInput():
	global ballX, barX
	# print("\n".join(["".join(line) for line in screen]))
	return 1 if ballX > barX else (-1 if ballX < barX else 0)

def processOutput(output):
	global outputs, score
	outputs.append(output)
	if len(outputs) == 3 and outputs[0] == -1 and outputs[1] == 0:
		score = outputs[2]
		outputs = []
	elif len(outputs) == 3:
		addPixel(outputs[0], outputs[1], outputs[2])
		outputs = []

runProgram(program, processInput, processOutput)
print(score)