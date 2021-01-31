from copy import deepcopy
from aocd import get_data

data = [[c[0], int(c[1])] for c in list(map(str.split, get_data(day=8, year=2020).splitlines()))]

def run_program(program: list, mutation: int):
	if mutation > -1:
		program[mutation][0] = "jmp" if program[mutation][0] == "nop" else "nop"
	acumulator = pointer = 0
	current_command = program[pointer]

	while len(current_command) == 2:
		if current_command[0] == "acc":
			acumulator += current_command[1]

		pointer += current_command[1] if current_command[0] == "jmp" else 1

		if pointer == len(program) - 1:
			return acumulator

		current_command.append("*")
		current_command = program[pointer]

	return False or acumulator

# Part 1
print(run_program(deepcopy(data), -1))

# Part 2
for m in range(len(data)):
	result = run_program(deepcopy(data), m)
	if result:
		print(result)
		break
