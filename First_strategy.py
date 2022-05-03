import AIStrat


def MAX (board,player):

	movesList = AIStrat.movePossibles(board)

	if gameOver(board):
		return utility(board)#, None


	else:

		meilleur_coup= None
		meilleur_score= float ("-inf")

		for move in movesList:
			successor = apply(move,board)
			score,_ = MIN(successor,1)
			if score > meilleur_score :
				meilleur_coup = move
				meilleur_score = score

		return meilleur_score ,meilleur_coup




def MIN (board,player):


	movesList_Adv = AIStrat.movePossibles([board[1],board[0]])

	if gameOver(board):
		return utility(board)#, None


	else:

		meilleur_coup= None
		meilleur_score= float ("inf")

		for move in movesList_Adv:
			successor = apply(move, board)
			score,_ = MAX(successor,1)
			if score < meilleur_score :
				meilleur_coup = move
				meilleur_score = score

		return meilleur_score, meilleur_coup

def caseCatch(case,dir, board, listPiece):
	case = AIStrat.caseDacote(case,dir)
	if case in board[1]:
		listPiece.append(case)
		return caseCatch(case, dir, board, listPiece)
	elif case in board[0]:
		return listPiece
	elif case is None:
		return []
	else:
		return []

def apply(move, board):
	boardJ = set(board[0])
	boardA = set(board[1])
	for dir in AIStrat.directionList:
		pieceCapture = caseCatch(move[0],dir,board,[])
		for piece in pieceCapture:
			boardJ.add(piece)
			boardA.remove(piece)
	boardJ.add(move[0])
	return [list(boardJ), list(boardA)]



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


def Strat (board):
	return MAX(board,0)

print(Strat([[28, 35],[27, 36]]))









	





