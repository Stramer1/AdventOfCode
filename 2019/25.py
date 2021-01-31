from itertools import chain, combinations
from aocd import get_data
from intcode import run_program

program = list(map(int, get_data(day=25, year=2019).split(',')))
text = previous_location = previous_move = starting_point = ""
directions = ["north", "east", "south", "west"]
combinations_list, dont_take_items, holding_items = [], ["photons", "escape pod", "molten lava", "infinite loop", "giant electromagnet"], []
visit_counter = 0
locations = {}

class Location:
	def __init__(self, name: str, items: list, doors: int):
		self.name = name
		self.items = items
		self.doors = doors
		self.neighbours = {}
		self.visited = 0

def parse_text():
	global text
	doors, items = [], []
	listing_doors = location = 0

	for line in text.splitlines():
		if "==" in line:
			location = line[3:-3]
		elif line == "Doors here lead:":
			listing_doors = 1
		elif listing_doors == 1 and "- " in line:
			doors.append(line[2:])
		elif line == "Items here:":
			listing_doors = 2
		elif listing_doors == 2 and "- " in line:
			items.append(line[2:])
	return location, doors, items

def choose_next_move(location_name: str, doors: list, items: list):
	global previous_location, previous_move, holding_items, dont_take_items, visit_counter, combinations_list, starting_point

	if location_name not in locations:
		locations[location_name] = Location(location_name, items, len(doors))
	if starting_point == "":
		starting_point = locations[location_name]

	visit_counter += 1
	locations[location_name].visited = visit_counter
	print(location_name, visit_counter, holding_items)
	if previous_move and previous_move not in previous_location.neighbours:
		previous_location.neighbours[previous_move] = locations[location_name]
		locations[location_name].neighbours[directions[(directions.index(previous_move)+2)%4]] = previous_location

	item_action = ""
	if combinations_list == [] and items != [] and items[0] not in dont_take_items:
		# print(items[0])
		holding_items.append(items[0])
		item_action = f"take {items[0]}\n"

	# If I haven't gone for a door before
	for move in doors:
		if move not in locations[location_name].neighbours:
			previous_location = locations[location_name]
			previous_move = move
			print(item_action + move)
			return item_action + move

	# If there are rooms to visit apart from Security Checkpoint
	if not all(l.doors == len(l.neighbours) for l in locations.values() if l.name != "Security Checkpoint") or location_name != "Security Checkpoint":
		# Choose the least visited door
		move = min(locations[location_name].neighbours, key=lambda x: locations[location_name].neighbours[x].visited)
		previous_location = locations[location_name]
		previous_move = move
		print(item_action + move)
		return item_action + move

	if combinations_list == []:
		combinations_list = chain(*map(lambda x: combinations(holding_items, x), range(4, len(holding_items))))

	combination = next(combinations_list)
	for item in holding_items:
		if item not in combination:
			holding_items.remove(item)
			item_action += f"drop {item}\n"
	for item in combination:
		if item not in holding_items:
			holding_items.append(item)
			item_action += f"take {item}\n"
	# print(holding_items)
	print(item_action + "south")
	return item_action + "south"



def process_input():
	global text, input_list, input_index
	if "You don't have that item." in text:
		return
	elif input_index == len(input_list) - 1:
		input_list = list(map(ord, choose_next_move(*parse_text()))) + [ord("\n")]
		input_index = 0
	else:
		input_index += 1
	if "Command?\n" in text:
		# print(text)
		text = ""
	return input_list[input_index]

def process_output(output: int):
	global text
	text += chr(output)

while True:
	input_index = -1
	input_list = []
	text = ""
	run_program(program, process_input, process_output)



# coin
# cake
# weather machine
# ornament
# jam
# food ration
# sand
# astrolabe