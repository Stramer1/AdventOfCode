from aocd import get_data

data = list(map(int, get_data(day=23, year=2020))) + list(range(10, 1000001))

class Number:
	def __init__(self, number: int, next_number: int):
		self.number = number
		self.next = next_number

# Create a Linked List
numbers = {data[len(data) - 1]: Number(data[len(data) - 1], 0)}
for i in range(len(data)-2, -1, -1):
	numbers[data[i]] = Number(data[i], numbers[data[i + 1]])
numbers[data[len(data) - 1]].next = numbers[data[0]]

current_element = numbers[data[0]]
for _ in range(10000000):
	first = current_element.next
	second = first.next
	third = second.next

	searching_for = current_element.number - 1 if current_element.number - 1 > 0 else len(data)

	while searching_for in (first.number, second.number, third.number):
		searching_for = searching_for - 1 if searching_for - 1 > 0 else len(data)

	current_element.next = third.next
	third.next = numbers[searching_for].next
	numbers[searching_for].next = first

	current_element = current_element.next

# c = numbers[1]
# answer = ""
# while c.next.number != 1:
# 	answer += str(c.next.number)
# 	c = c.next
# print(answer)

print(numbers[1].next.number * numbers[1].next.next.number)