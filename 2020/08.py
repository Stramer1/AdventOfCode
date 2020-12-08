from aocd import get_data
from copy import deepcopy

program = [[command[0], int(command[1])] for command in list(map(str.split, get_data(day=8, year=2020).splitlines()))]
programCopy = deepcopy(program)

acumulator = pointer = 0
currentCommand = program[pointer]

while len(currentCommand) == 2:
	if currentCommand[0] == "acc":
		acumulator += currentCommand[1]

	pointer += currentCommand[1] if currentCommand[0] == "jmp" else 1
	currentCommand.append("*")
	currentCommand = program[pointer]

print(acumulator)

def runProgram(program, mutation):
	program[mutation][0] = "jmp" if program[mutation][0] == "nop" else "nop" 
	acumulator = pointer = 0
	currentCommand = program[pointer]

	while len(currentCommand) == 2:
		if currentCommand[0] == "acc":
			acumulator += currentCommand[1]

		pointer += currentCommand[1] if currentCommand[0] == "jmp" else 1

		if pointer == len(program) - 1:
			return acumulator

		currentCommand.append("*")
		currentCommand = program[pointer]

	return False


for mutation in range(len(program)):
	result = runProgram(deepcopy(programCopy), mutation)
	if result:
		print(result)
		break