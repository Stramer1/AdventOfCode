from aocd import get_data
from re import match

data = get_data(day=16, year=2020).split("\n\n")

# The 2 ranges are [0] to [1] and [2] to [3], field name is in [5]
# The set in [4] are the indexes of the ticket that cannot be that field
ticketFields = []
for line in data[0].splitlines():
	matches = match("(.*): (.*)-(.*) or (.*)-(.*)", line).groups()
	ticketFields.append(list(map(int, matches[1:])) + [set(), matches[0]])

myTicket = list(map(int, data[1].splitlines()[1].split(",")))
nearbyTickets = [list(map(int, line.split(","))) for line in data[2].splitlines()[1:]]

def belongsToField(ticketField, number):
	return ticketField[0] <= number <= ticketField[1] or ticketField[2] <= number <= ticketField[3]

errorRate = 0
for ticket in nearbyTickets:
	for number in range(len(ticket)):
		# If number does not belong to any field then the ticket in invalid 
		if not any([belongsToField(ticketField, ticket[number]) for ticketField in ticketFields]):
			errorRate += ticket[number]
		else:
			for ticketField in ticketFields:
				if not belongsToField(ticketField, ticket[number]):
					ticketField[4].add(number)

# Sort by the length of the list of impossible indexes in ticket
ticketFields = sorted(ticketFields, key=lambda ticketField: len(ticketField[4]), reverse = True)
dic = {ticketField[5]: [possible for possible in range(len(myTicket)) if possible not in ticketField[4]] for ticketField in ticketFields}
# {Field Name: Possible indexes in ticket}

total = 1
for element in dic:
	# Since the list of possible indexes in ticket is always equal to the previous + the correct element
	dic[element] = list(filter(lambda x: x not in dic.values(), dic[element]))[0]
	if element.startswith("departure"):
		total *= myTicket[dic[element]]

print(errorRate)
print(total)