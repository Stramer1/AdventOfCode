from aocd import get_data

data = list(map(int, get_data(day=1, year=2019).splitlines()))

total = 0
for module in data:
	total += module//3-2
print(total)

total = 0
for module in data:
	fuel = module
	while fuel > 8:
		fuel = fuel//3-2
		total += fuel
print(total)