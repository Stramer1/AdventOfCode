from aocd import get_data
from intcode import runProgram

program = list(map(int, get_data(day=19, year=2019).split(',')))
totalPulled = counter = xTurn = cornersIndex = previousOutput = foundBeam = 0
corners = coordinate = [500, 0]
answerNotFound = True
size = 50

def processInput1():
	global counter, xTurn
	xTurn = not xTurn
	return counter // size if xTurn else counter % size

def processOutput1(output):
	global totalPulled, counter
	counter += 1
	totalPulled += output

while counter < size * size:
	runProgram(program, processInput1, processOutput1)

print(totalPulled)

def calculateOpositeCorner(coordinate):
	return  [coordinate[0] + 99, coordinate[1] - 99] + coordinate

def processInput2():
	global corners, cornersIndex
	cornersIndex += 1
	return corners[cornersIndex - 1]

def processOutput2(output):
	global previousOutput, cornersIndex, coordinate, corners, answerNotFound, foundBeam
	
	if cornersIndex == len(corners):
		if not foundBeam and output == 0:
			corners = coordinate = [coordinate[0], coordinate[1] + 1]
		elif not foundBeam and output == 1:
			foundBeam = True
			corners = coordinate = [coordinate[0], coordinate[1] + 1]
		elif foundBeam and output == 0:
			coordinate = [coordinate[0] + 1, coordinate[1] - 2]
			corners = calculateOpositeCorner(coordinate)
		elif foundBeam and previousOutput == 0 and output == 1:
			coordinate = [coordinate[0], coordinate[1] + 1]
			corners = calculateOpositeCorner(coordinate)
		elif foundBeam and output == previousOutput == 1:
			answerNotFound = False
		cornersIndex = previousOutput = 0
	else:
		previousOutput = output

while answerNotFound:
	runProgram(program, processInput2, processOutput2)

print(coordinate[0] * 10000 + coordinate[1] - 99)