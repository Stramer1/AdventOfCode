from aocd import get_data

data = get_data(day=18, year=2020).splitlines()

def evaluate1(line):
	while isinstance(line, str) and "(" in line:
		lastIndex = line.find(")")
		firstIndex = line[:lastIndex].rfind("(")
		line = line[:firstIndex] + str(evaluate1(line[firstIndex+1:lastIndex])) + line[lastIndex+1:]
	while isinstance(line, str) and ("*" in line or "+" in line):
		index = max(line.rfind("*"), line.rfind("+"))
		if index == line.rfind("*"):
			line = evaluate1(line[:index]) * evaluate1(line[index+1:])
		else:
			line = evaluate1(line[:index]) + evaluate1(line[index+1:])
	return int(line)

def evaluate2(line):
	while isinstance(line, str) and "(" in line:
		lastIndex = line.find(")")
		firstIndex = line[:lastIndex].rfind("(")
		line = line[:firstIndex] + str(evaluate2(line[firstIndex+1:lastIndex])) + line[lastIndex+1:]
	while isinstance(line, str) and "*" in line:
		index = line.find("*")
		line = evaluate2(line[:index]) * evaluate2(line[index+1:])
	while isinstance(line, str) and "+" in line:
		index = line.find("+")
		line = evaluate2(line[:index]) + evaluate2(line[index+1:])
	return int(line)


print(sum([evaluate1(line.replace(" ", "")) for line in data]))
print(sum([evaluate2(line.replace(" ", "")) for line in data]))