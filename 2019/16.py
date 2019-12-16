from aocd import get_data

data = get_data(day=16, year=2019)[:-1]
digitList = list(map(int, data))
startingPattern = [0, 1, 0, -1]

for _ in range(100):
	digitListCopy = []
	for line in range(len(digitList)):
		pattern = []
		for number in startingPattern:
			pattern += (line+1) * [number]

		total = 0
		for index, value in enumerate(digitList):
			total += value * pattern[(index+1) % len(pattern)]
		digitListCopy.append(abs(total)%10)
	digitList = digitListCopy


print("".join(map(str, digitList[:8])))


data = data * 10000
digitList = map(int, data[int(data[:7]):][::-1])

for _ in range(100):
	digitListCopy = []
	total = 0
	for digit in digitList:
		total += digit
		digitListCopy.append(total % 10)
	digitList = digitListCopy

print("".join(map(str,digitList[::-1][:8])))