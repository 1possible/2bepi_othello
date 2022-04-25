import random

from game import possibleMoves, Othello , next
from status import MatchStatus



def random_strategy(state):

	return random.choice(possibleMoves(state))    # Stratégie random pour test connexion IA


Game = Othello

if __name__ == '__main__':

	state, next = Game(['Player1', 'Player2'])
	move = 26

	print(next(state,move))



def run_AI(fun):

	while True:

		if MatchStatus.DONE == 3 :  # Game is done.
			print()

		else:

			move = random_strategy(state)
			print("{} {}".format(move))


if __name__ == "__main__":
	run_AI()



