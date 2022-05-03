import AIStrat


def MAX (board,player):

	movesList = AIStrat.movePossibles(board)

	if gameOver(board):
		return utility(board), None


	else:

		meilleur_coup= None
		meilleur_score= float ("-inf")

		for move in movesList:
			successor = apply(board, move)
			score,_ = MIN(board)
			if score > meilleur_score :
				meilleur_coup = move
				meilleur_score = score

		return meilleur_score ,meilleur_coup




def MIN (board,player):


	movesList_Adv = AIStrat.movePossibles([board[1],board[0]])

	if gameOver(board):
		return utility(board), None


	else:

		meilleur_coup= None
		meilleur_score= float ("inf")

		for move in movesList_Adv:
			successor = apply(board, move)
			score,_ = MAX(board)
			if score < meilleur_score :
				meilleur_coup = move
				meilleur_score = score

		return meilleur_score, meilleur_coup




def Strat (board):
	return MAX(board)


def gameOver (board):

	if len(board[0])+len(board[1]) == 64:
		return True

	elif len (AIStrat.movePossibles(board)) == 0 and (AIStrat.movePossibles([board[1],board[0]])) == 0: 
		return True 

	else:
		return False

def utility (board):

	if len (board[0]) > len (board[1]):
		return 1

	else: 
		return -1









	





