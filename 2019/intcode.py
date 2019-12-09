from copy import deepcopy

def write(program, position, value):
	if position >= len(program):
		program += [0] * (position - len(program) + 1)
	program[position] = value

def read(program, position):
	if position >= len(program):
		program += [0] * (position - len(program) + 1)
	return program[position]

def getParameter(program, pointer, parameter, relativeBase):
	if read(program, pointer)//10**(parameter+1)%10 == 1:
		return pointer + parameter
	elif read(program, pointer)//10**(parameter+1)%10 == 2:
		return read(program, pointer + parameter) + relativeBase
	else:
		return read(program, pointer + parameter)

def runProgram(program, processInput, processOutput, condition = lambda: True):
	pointer = relativeBase = 0
	program = deepcopy(program)
	
	while condition() and read(program, pointer) != 99:
		instruction = read(program, pointer)%100
		param1 = getParameter(program, pointer, 1, relativeBase)
		param2 = getParameter(program, pointer, 2, relativeBase)
		param3 = getParameter(program, pointer, 3, relativeBase)

		if instruction == 1:
			write(program, param3, read(program, param1) + read(program, param2))
			pointer += 4
		elif instruction == 2:
			write(program, param3, read(program, param1) * read(program, param2))
			pointer += 4
		elif instruction == 3:
			write(program, param1, processInput())
			pointer += 2
		elif instruction == 4:
			processOutput(read(program, param1))
			pointer += 2
		elif instruction == 5:
			if read(program, param1):
				pointer = read(program, param2)
			else:
				pointer += 3
		elif instruction == 6:
			if not read(program, param1):
				pointer = read(program, param2)
			else:
				pointer += 3
		elif instruction == 7:
			write(program, param3, 1 if read(program, param1) < read(program, param2) else 0)
			pointer += 4
		elif instruction == 8:
			write(program, param3, 1 if read(program, param1) == read(program, param2) else 0)
			pointer += 4
		elif instruction == 9:
			relativeBase += read(program, param1)
			pointer += 2
		else:
			print("Error")