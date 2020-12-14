from aocd import get_data

data = get_data(day=14, year=2020).splitlines()
memory1, memory2 = {}, {}

def decode1(mask, value):
	for digit in range(36):
		if mask[digit] == "X":
			mask = mask[:digit] + value[digit] + mask[digit+1:]
	return int(mask.replace("X", "0"), 2)

def decode2(mask, address):
	for digit in range(36):
		if mask[digit] != "0":
			address = address[:digit] + mask[digit] + address[digit+1:]
	return address 

def calculateAddresses(address):
	if "X" in address:
		return calculateAddresses(address.replace("X", "0", 1)) + calculateAddresses(address.replace("X", "1", 1))
	else:
		return [int(address,2)]

for line in data:
	values = line.split(" = ")
	if values[0] == "mask":
		mask = values[1]
	else:
		address = bin(int(values[0][4:-1]))[2:]
		address = "0" * (36 - len(address)) + address
		
		value = bin(int(values[1]))[2:]
		value = "0" * (36 - len(value)) + value

		memory1[address] = decode1(mask, value)
		address = decode2(mask, address)

		for address in calculateAddresses(address):
			memory2[address] = int(value, 2)

print(sum(memory1.values()))
print(sum(memory2.values()))