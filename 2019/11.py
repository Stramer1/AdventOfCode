from aocd import get_data
from intcode import run_program

program = list(map(int, get_data(day=11, year=2019).split(',')))
panels = {}
location = [0, 0]
output_is_color = True
looking = (0, -1)
panels[str(location)] = 1

def process_input():
	global panels, location
	if str(location) not in panels:
		panels[str(location)] = 0
	return panels[str(location)]

def process_output(output):
	global panels, location, output_is_color, looking
	if output_is_color:
		panels[str(location)] = output
	elif output:
		looking = (-looking[1], looking[0])
		location = [location[0] + looking[0], location[1] + looking[1]]
	else:
		looking = (looking[1], - looking[0])
		location = [location[0] + looking[0], location[1] + looking[1]]
	output_is_color = not output_is_color

run_program(program, process_input, process_output)

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