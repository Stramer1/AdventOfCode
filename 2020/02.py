from re import findall
from aocd import get_data

data = get_data(day=2, year=2020).splitlines()

valid = 0
for line in data:
	mini, maxi, char, word = findall(r"(\d+)-(\d+) (.): (.*)", line)[0]
	mini, maxi = int(mini),int(maxi)

	if mini <= word.count(char) <= maxi:
		valid+=1
print(valid)

valid = 0
for line in data:
	i1, i2, char, word = findall(r"(\d+)-(\d+) (.): (.*)", line)[0]
	i1, i2 = int(i1) - 1, int(i2) - 1

	if (word[i1] == char) + (word[i2]  == char) == 1:
		valid+=1
print(valid)