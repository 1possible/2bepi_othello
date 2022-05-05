import AIStrat


def MAX (board,player):

	movesList = AIStrat.movePossibles(board)

	if gameOver(board):
		return utility(board), None


	else:

		meilleur_coup= None
		meilleur_score= float ("-inf")

		for move in movesList[0]:
			successor = apply(move,board)
			score,_ = MIN([successor[1],successor[0]],1)
			if score > meilleur_score :
				meilleur_coup = move
				meilleur_score = score

		return meilleur_score ,meilleur_coup




def MIN (board,player):


	movesList_Adv = AIStrat.movePossibles(board)

	if gameOver(board):
		return utility(board), None


	else:

		meilleur_coup= None
		meilleur_score= float ("inf")

		for move in movesList_Adv[0]:
			successor = apply(move, board)
			score,_ = MAX([successor[1],successor[0]],1)
			if score < meilleur_score :
				meilleur_coup = move
				meilleur_score = score

		return meilleur_score, meilleur_coup


def negamax(board):

	movesList = AIStrat.movePossibles(board)

	if gameOver(board):
		return -utility(board), None

	meilleur_score, meilleur_coup = float('-inf'), None
	for move in movesList[0]:
		successor = apply(move,board)
		score, _ = negamax([successor[1],successor[0]])
		if score > meilleur_score:
			meilleur_score, meilleur_coup = score, move
	return -meilleur_score, meilleur_coup

def negamaxLimitedDepth(board,depth=1):

	movesList = AIStrat.movePossibles(board)

	if gameOver(board) or depth==0:
		return -heuristic(board), None

	meilleur_score, meilleur_coup = float('-inf'), None
	for move in movesList[0]:
		successor = apply(move,board)
		score, _ = negamaxLimitedDepth([successor[1],successor[0]],depth-1)
		if score >= meilleur_score:
			meilleur_score, meilleur_coup = score, move
	return -meilleur_score, meilleur_coup


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
		pieceCapture = caseCatch(move,dir,board,[])
		for piece in pieceCapture:
			boardJ.add(piece)
			boardA.remove(piece)
	boardJ.add(move)
	return [list(boardJ), list(boardA)]



def gameOver (board):

	if len(board[0])+len(board[1]) == 64:
		return True

	elif len (AIStrat.movePossibles(board)[0]) == 0 and (AIStrat.movePossibles([board[1],board[0]])[0]) == 0:
		return True 

	else:
		return False

def utility (board):

	if len (board[0]) > len (board[1]):
		return 1

	else: 
		return -1


def heuristic(board):

	if gameOver(board):

		if len (board[0]) > len (board[1]):
			return float("inf")

		else: 
			return float ("-inf")

	h=0
	if len(board[0])+len(board[1]) >25:
		h += len (board[0]) - len(board[1])
	pionIntouchable = 0
	for pion in board[0]:
		if(AIStrat.pionIntouchable(pion,board)):
			pionIntouchable+=1
	h+=pionIntouchable
	return h



	
		


	










def Strat (board):
	return negamaxLimitedDepth(board)


#print(Strat([[28, 35],[27, 36]]))

#print(Strat([[8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61],
        [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
          45, 46, 49, 50, 53, 54, 55, 62, 63]]))
#print(Strat([[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
          45, 46, 49, 50, 53, 54, 55, 62, 63],[8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61],
         ]))









	





