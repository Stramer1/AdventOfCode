from aocd import get_data
from intcode import run_program

program = list(map(int, get_data(day=9, year=2019).split(',')))

def process_input():
	return int(input())

def process_output(output):
	print(output)

run_program(program, process_input, process_output)
