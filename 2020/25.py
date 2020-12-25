from aocd import get_data

doorpublicKey, cardpublicKey = list(map(int, get_data(day=25, year=2020).splitlines()))
doorloopSize = 0

value = 1
while value != doorpublicKey:
	value = value * 7 % 20201227
	doorloopSize += 1
	print(doorloopSize, end="\r")

value = 1
for _ in range(doorloopSize):
	value = value * cardpublicKey % 20201227

print(f"\n{value}")