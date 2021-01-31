from aocd import get_data

data = get_data(day=19, year=2020).split("\n\n")
rules = {}

for line in data[0].replace("8: 42", "8: 42 | 42 8").replace("11: 42 31", "11: 42 31 | 42 11 31").splitlines():
	rule = line.split(": ")
	if '"' in rule[1]:
		rules[rule[0]] = rule[1][1:-1]
	elif '|' in rule[1]:
		rules[rule[0]] = [possibility.split() for possibility in rule[1].split(" | ")]
	else:
		rules[rule[0]] = [rule[1].split()]

def match(string, rule, pending):
	if isinstance(rules[rule], str):
		if pending == [] and len(string) == 1 and string[0] == rules[rule]:
			return True
		elif pending != [] and len(string) > 0 and string[0] == rules[rule]:
			return match(string[1:], pending[0], pending[1:])
		else:
			return False
	else:
		return any([match(string, possibility[0], possibility[1:] + pending) for possibility in rules[rule]])

print(sum([match(message, "0", []) for message in data[1].splitlines()]))