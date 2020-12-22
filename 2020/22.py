from aocd import get_data
from collections import deque

data = [list(map(int, player.splitlines()[1:])) for player in get_data(day=22, year=2020).split("\n\n")]
player1, player2 = deque(data[0]), deque(data[1])

def play(player1, player2):
	states = []
	while len(player1) != 0 and len(player2) != 0:
		if repr(player1) + repr(player2) in states:
			return 1
		else:
			states.append(repr(player1) + repr(player2))
			
		a, b = player1.popleft(), player2.popleft()

		if len(player1) >= a and len(player2) >= b:
			copy1, copy2 = player1.copy(), player2.copy()
			while len(copy1) != a:
				copy1.pop()
			while len(copy2) != b:
				copy2.pop()
			winner = play(copy1, copy2)
		else:
			winner = 1 if a > b else 2

		if winner == 1:
			player1.extend([a, b])
		else:
			player2.extend([b, a])

	return 1 if len(player2) == 0 else 2

winner = player1 if play(player1, player2) == 1 else player2
print(sum(winner.pop() * i for i in range(1, len(winner)+1)))
