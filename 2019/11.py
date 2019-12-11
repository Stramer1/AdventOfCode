from aocd import get_data
from intcode import runProgram

program = list(map(int, get_data(day=11, year=2019).split(',')))
panels = {}
location = [0, 0]
outputIsColor = True
looking = (0, -1)
panels[str(location)] = 1

def processInput():
	global panels, location
	if str(location) not in panels:
		panels[str(location)] = 0
	return panels[str(location)]

def processOutput(output):
	global panels, location, outputIsColor, looking
	if outputIsColor:
		panels[str(location)] = output
	elif output:
		looking = (-looking[1], looking[0])
		location = [location[0] + looking[0], location[1] + looking[1]]
	else:
		looking = (looking[1], - looking[0])
		location = [location[0] + looking[0], location[1] + looking[1]]
	outputIsColor = not outputIsColor

intcode.runProgram(program, processInput, processOutput)

panels2 = []
print(len(panels))

for string in panels:
	coordinates = string.split(", ")
	x = int(coordinates[0][1:])
	y = int(coordinates[1][:-1])
	while len(panels2) <= y:
		panels2.append([])
	while len(panels2[y]) <= x:
		panels2[y].append([])
	panels2[y][x] = panels[string]

for line in panels2:
	print("".join(["#" if digit == 1 else " " for digit in line]))