from aocd import get_data
from re import search
from re import findall

data = get_data(day=7, year=2020).splitlines()
# wavy olive bags contain 1 striped olive bag, 1 dull cyan bag.
# plaid cyan bags contain no other bags.

rules = []
for line in data:
	container = search(r"(.*) bags contain", line).group(1)
	contents = findall(r"(\d+) (.*?) bag", line)
	rules.append([container, contents])

# ['wavy beige', [('5', 'muted silver'), ('5', 'pale teal')]]

lookingFor = ["shiny gold"]
originalLength = 0

while originalLength != len(lookingFor):
	originalLength = len(lookingFor)
	for rule in rules:
		if rule[-1] != "*" and set(lookingFor).intersection([content[1] for content in rule[1]]):
			lookingFor.append(rule[0])
			rule.append("*")

print(len([rule for rule in rules if rule[-1] == "*"]))

def recursiveSearch(bag):
	for rule in rules:
		if rule[0] == bag:
			return 1 + sum([int(contents[0]) * recursiveSearch(contents[1]) for contents in rule[1]])

print(recursiveSearch("shiny gold") - 1)