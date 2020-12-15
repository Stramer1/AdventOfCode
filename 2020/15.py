from aocd import get_data

data = list(map(int, get_data(day=15, year=2020).split(",")))
dic = {element: data.index(element) for element in data}
length = len(data)
currentElement = 0

while length < 30000000-1:
	if currentElement in dic:
		index = dic[currentElement]
		dic[currentElement] = length
		currentElement = length - index
	else:
		dic[currentElement] = length
		currentElement = 0
	length += 1

	if length == 2019:
		print(currentElement)
print(currentElement)

