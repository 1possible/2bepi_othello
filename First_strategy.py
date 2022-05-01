import AIStrat


def MAX (board):

	movesList = AIStrat.movePossibles(board)
	if len(movesList) == 0:
		return None

	else:

		meilleur_coup= None
		meilleur_score= float ("-inf")

		for move in movesList:
			score,_ = MIN(board)
			if score > meilleur_score :
				meilleur_coup = move
				meilleur_score = score

		return meilleur_score ,meilleur_coup

def MIN (board):


	movesList_Adv = AIStrat.movePossibles([board[1],board[0]])
	if len(movesList_Adv) == 0:
		return None

	else:

		meilleur_coup= None
		meilleur_score= float ("-inf")

		for move in movesList_Adv:
			
			score,_ = MAX(board)
			if score < meilleur_score :
				meilleur_coup = move
				meilleur_score = score

		
		return meilleur_score, meilleur_coup




def Strat (board):
	return MAX(board)

