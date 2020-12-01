from aocd import get_data

data = list(map(int, get_data(day=1, year=2020).splitlines()))

for element in data:
	if 2020 - element in data:
		print(element * (2020 - element))
		break

for i1 in range(len(data)):
	for i2 in range(i1, len(data)):
		for i3 in range(i2, len(data)):
			if (data[i1] + data[i2] + data[i3] == 2020):
				print(data[i1] * data[i2] * data[i3])