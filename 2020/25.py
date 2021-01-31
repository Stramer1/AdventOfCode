from aocd import get_data

doorpublic_key, cardpublic_key = list(map(int, get_data(day=25, year=2020).splitlines()))
doorloop_size = 0

value = 1
while value != doorpublic_key:
	value = value * 7 % 20201227
	doorloop_size += 1
	print(doorloop_size, end="\r")

value = 1
for _ in range(doorloop_size):
	value = value * cardpublic_key % 20201227

print(f"\n{value}")