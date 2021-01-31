from aocd import get_data

program = list(map(int, get_data(day=5, year=2019).split(',')))

program_output = pointer = 0
input_value = 1

while program[pointer] != 99 and not program_output:
	instruction = program[pointer]%100
	param1 = pointer + 1 if program[pointer]//100%10 else program[pointer + 1]
	param2 = pointer + 2 if program[pointer]//1000 else program[pointer + 2]
	param3 = program[pointer + 3]

	if instruction == 1:
		program[param3] = program[param1] + program[param2]
		pointer += 4
	elif instruction == 2:
		program[param3] = program[param1] * program[param2]
		pointer += 4
	elif instruction == 3:
		program[param1] = input_value
		pointer += 2
	elif instruction == 4:
		program_output = program[param1]
		pointer += 2
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
print(program_output)