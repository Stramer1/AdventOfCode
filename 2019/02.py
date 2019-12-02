from aocd import get_data
from copy import deepcopy

program = list(map(int, get_data(day=2, year=2019).split(',')))

def runProgram(program, noun, verb):
	program[1] = noun
	program[2] = verb
	pointer = 0
	while program[pointer] != 99:
		if program[pointer] == 1:
			program[program[pointer + 3]] = program[program[pointer + 1]] + program[program[pointer + 2]]
		elif program[pointer] == 2:
			program[program[pointer + 3]] = program[program[pointer + 1]] * program[program[pointer + 2]]
		pointer += 4
	return program[0]

print(runProgram(deepcopy(program), 12, 2))

for noun in range(100):
	for verb in range(100):
		if runProgram(deepcopy(program), noun, verb) == 19690720:
			print(noun * 100 + verb)
