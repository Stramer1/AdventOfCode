from aocd import get_data
from itertools import permutations
from copy import deepcopy

amplifier = [list(map(int, get_data(day=7, year=2019).split(','))), 0]

def runAmplifier(amplifier, *inputs):
	program = amplifier[0]
	pointer = amplifier[1]
	inputIndex = 0
	while program[pointer] != 99:
		instruction = program[pointer]%100
		param1 = pointer + 1 if program[pointer]//100%10 else program[pointer + 1]
		param2 = pointer + 2 if program[pointer]//1000 else program[pointer + 2]
		if pointer + 3 < len(program):
			param3 = program[pointer + 3]

		if instruction == 1:
			program[param3] = program[param1] + program[param2]
			pointer += 4
		elif instruction == 2:
			program[param3] = program[param1] * program[param2]
			pointer += 4
		elif instruction == 3:
			program[param1] = inputs[inputIndex]
			inputIndex += 1
			pointer += 2
		elif instruction == 4:
			amplifier[1] = pointer + 2
			return True, program[param1]
		elif instruction == 5:
			if program[param1]:
				pointer = program[param2]
			else:
				pointer += 3
		elif instruction == 6:
			if not program[param1]:
				pointer = program[param2]
			else:
				pointer += 3
		elif instruction == 7:
			if program[param1] < program[param2]:
				program[param3] = 1
			else:
				program[param3] = 0
			pointer += 4
		elif instruction == 8:
			if program[param1] == program[param2]:
				program[param3] = 1
			else:
				program[param3] = 0
			pointer += 4
	return False, inputs[inputIndex]

maximum = 0
for permutation in list(permutations([0, 1, 2, 3, 4])):
	output = 0
	for phase in permutation:
		boolean, output = runAmplifier(deepcopy(amplifier), phase, output)
	maximum = max(maximum, output)
print(maximum)

maximum = 0
for permutation in list(permutations([5, 6, 7, 8, 9])):
	amplifiers = [deepcopy(amplifier),
				  deepcopy(amplifier),
				  deepcopy(amplifier),
				  deepcopy(amplifier),
				  deepcopy(amplifier)]
	output = 0
	for phase in range(5):
		amplifierRunning, output = runAmplifier(amplifiers[phase], permutation[phase], output)

	while amplifierRunning:
		for phase in range(5):
			amplifierRunning, output = runAmplifier(amplifiers[phase], output)
		maximum = max(maximum, output)
print(maximum)