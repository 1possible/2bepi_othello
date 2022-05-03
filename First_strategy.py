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

def caseCatch(case,dir, board, listPiece=[]):
	case = AIStrat.caseDacote(case,dir)
	if case in board[1]:
		listPiece.append(case)
		return move(case, dir, board, listPiece)
	elif case in board[0]:
		return listPiece
	elif case is None:
		return []
	else:
		return []

def apply(move, board):
	boardJ = set(board[1])
	boardA = set(board[2])
	for dir in AIStrat.directionList:
		pieceCapture = caseCatch(move,dir,board)
		for piece in pieceCapture:
			boardJ.add(piece)
			boardA.remove(piece)
	return [list(boardJ), list(boardA)]




def Strat (board):
	return MAX(board)

