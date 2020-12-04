from aocd import get_data
from re import search

data = [line.replace("\n", " ") for line in get_data(day=4, year=2020).split("\n\n")]
# hcl:#fffffd byr:1951 cid:321 iyr:2017 eyr:2022 ecl:brn hgt:62in pid:#6ef4e1

valid = 0
for passport in data:
	if "pid:" in passport and "ecl:" in passport and "hcl:" in passport and "hgt:" in passport and "eyr:" in passport and "iyr:" in passport and "byr:" in passport:
		valid += 1
print(valid)


totalValid = 0
for passport in data:
	byr = search(r"byr:(\d{4})\b", passport)
	iyr = search(r"iyr:(\d{4})\b", passport)
	eyr = search(r"eyr:(\d{4})\b", passport)
	hgtcm = search(r"hgt:(\d+)cm\b", passport)
	hgtin = search(r"hgt:(\d+)in\b", passport)
	hcl = search(r"hcl:#[0-9a-f]{6}\b", passport)
	ecl = search(r"ecl:(...)\b", passport)
	pid = search(r"pid:(\d{9})\b", passport)

	valid = byr and iyr and eyr and hcl and ecl and pid
	valid = valid and 1920 <= int(byr.group(1)) <= 2002
	valid = valid and 2010 <= int(iyr.group(1)) <= 2020
	valid = valid and 2020 <= int(eyr.group(1)) <= 2030
	valid = valid and (hgtcm and 150 <= int(hgtcm.group(1)) <= 193 or hgtin and 59 <= int(hgtin.group(1)) <= 76)
	valid = valid and ecl.group(1) in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

	if (valid):
		totalValid += 1

print(totalValid)