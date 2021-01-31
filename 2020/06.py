from aocd import get_data

data = get_data(day=6, year=2020).split("\n\n")
print(sum(len(set(line.replace("\n", ""))) for line in data))

sum1 = 0
for group in data[:-1]:
	set1 = set(group)
	for individual in group.split("\n"):
		set1 = set1.intersection(individual)
	sum1 += len(set1)
print(sum1)