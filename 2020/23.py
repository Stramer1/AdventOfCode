from aocd import get_data

data = list(map(int, get_data(day=23, year=2020)[:-1])) + list(range(10, 1000001))
current = 0

class Number:
	def __init__(self, number, nextNumber):
		self.number = number
		self.next = nextNumber

# Create a Linked List
numbers = {data[len(data) - 1]: Number(data[len(data) - 1], 0)}
for i in range(len(data)-2, -1, -1):
	numbers[data[i]] = Number(data[i], numbers[data[i + 1]])
numbers[data[len(data) - 1]].next = numbers[data[0]]

currentElement = numbers[data[0]]
for _ in range(10000000):
	first = currentElement.next
	second = first.next
	third = second.next
	
	searchingFor = currentElement.number - 1 if currentElement.number - 1 > 0 else len(data)

	while searchingFor in (first.number, second.number, third.number):
		searchingFor = searchingFor - 1 if searchingFor - 1 > 0 else len(data)

	currentElement.next = third.next
	third.next = numbers[searchingFor].next
	numbers[searchingFor].next = first

	currentElement = currentElement.next 

# c = numbers[1]
# answer = ""
# while c.next.number != 1:
# 	answer += str(c.next.number)
# 	c = c.next
# print(answer)

print(numbers[1].next.number * numbers[1].next.next.number)