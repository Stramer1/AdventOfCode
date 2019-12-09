from aocd import get_data
from intcode import runProgram

program = list(map(int, get_data(day=9, year=2019).split(',')))
pointer = relativeBase = 0

def processInput():
	return int(input())

def processOutput(output):
	print(output)

runProgram(program, processInput, processOutput)