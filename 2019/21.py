from aocd import get_data
from intcode import run_program

program = list(map(int, get_data(day=21, year=2019).split(',')))
input_index = dust = alignment_total = facing_direction = 0
vectors = [(0, -1), (1, 0), (0, 1), (-1, 0)]
area = ""
path = []

def process_input():
	global input_index
	value = input_list[input_index]
	input_index += 1
	return value

def process_output(output):
	global area, dust
	dust = output
	area += chr(output)

run_program(program, process_input, process_output)