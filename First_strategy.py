import AIStrat


def MAX (board):

# Stratégie minimax
# Fonction pour joueur max

	movesList = AIStrat.movePossibles(board)

	if gameOver(board):
		return utility(board), None

	else:

		meilleur_coup= None
		meilleur_score= float ("-inf")

		for move in movesList[0]:
			successor = apply(move,board)
			score,_ = MIN([successor[1],successor[0]])
			if score > meilleur_score :
				meilleur_coup = move
				meilleur_score = score

		return meilleur_score ,meilleur_coup


def MIN (board):

# Stratégie minimax
# Fonction pour joueur min

	movesList_Adv = AIStrat.movePossibles(board)

	if gameOver(board):
		return utility(board), None

	else:

		meilleur_coup= None
		meilleur_score= float ("inf")

		for move in movesList_Adv[0]:
			successor = apply(move, board)
			score,_ = MAX([successor[1],successor[0]])
			if score < meilleur_score :
				meilleur_coup = move
				meilleur_score = score

		return meilleur_score, meilleur_coup


def negamax(board):

# Stratégie negamax 
# Fonction negamax combinant les fonctions max et min

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

# Stratégie negamax avec profondeur limitée

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



def negamaxWithPruning(board,alpha=float('-inf'), beta=float('inf')):

# Stratégie negamax avec pruning

	movesList = AIStrat.movePossibles(board)

	if gameOver(board):
		return -utility(board), None


	meilleur_score, meilleur_coup = float('-inf'), None
	for move in movesList[0]:
		successor = apply(move,board)
		score, _ = negamaxWithPruning([successor[1],successor[0]],-beta, -alpha)
		if score > meilleur_score:
			meilleur_score, meilleur_coup = score, move
		alpha = max(alpha,meilleur_score)
		if alpha >=beta:
			break
	return -meilleur_score, meilleur_coup

def negamaxWithPruningLimitedDepth(board,depth=2,alpha=float('-inf'), beta=float('inf')):

# Stratégie negamax avec pruning et profondeur limitée

	movesList = AIStrat.movePossibles(board)

	if gameOver(board) or depth==0:
		return -heuristic(board), None


	meilleur_score, meilleur_coup = float('-inf'), None
	for move in movesList[0]:
		successor = apply(move,board)
		score, _ = negamaxWithPruningLimitedDepth([successor[1],successor[0]],depth-1,-beta, -alpha)
		if score >= meilleur_score:
			meilleur_score, meilleur_coup = score, move
		alpha = max(alpha,meilleur_score)
		if alpha >=beta:
			break
	return -meilleur_score, meilleur_coup


def caseCatch(case,dir, board, listPiece):
#Fonction de capture de case 

#    Paramètres:
#       case        : int compris entre 0 et 63 inclus: case de référence
#       direction   : tuple avec comme premier élément -1,0,1 qui fait reference à la colonne
#                                      deuxiemme élément -1,0,1 qui fait référence à la ligne
#       board       : l'etat du plateau sour forme de list à 2 éléments
#                       board[0] :liste qui contient les cases de ses pieces
#                       board[1] : liste qui contient les cases des piece de son adversaire
#       listPiece   : liste des pions

#Elle regarde si la case qui se trouve à coté dans la direction :
#                                                               - est prise par l'adversaire --> elle ajoute la case à la liste des pions 
#                                                                 puis retourne la liste 
#                                                               - est prise par notre joueur --> elle retourne la liste des pions
#                                                               - n'est pas prise --> elle retourne une liste vide
# Sinon elle retourne une liste vide

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
# Fonction qui renvoie 2 ensembles avec comme paramètres le move (case à prendre) et l'état du plateau
# Les 2 ensembles :
# boardJ : ensemble des pions de notre joueur
# boardA : ensemble des pions de l'adversaire
# Pour une direction , ajout du pion capturé (se trouvant dans la liste de pions capturés) dans l'ensemble des pions de notre joueur
#                      + retrait de ce pion de l'ensemble des pions de l'adversaire
# Ajout du move dans l'ensemble des pions de notre joueur


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
# Fonction qui regarde si la partie est finie

# Si 
# - tous les pions sont sur le plateau
# - plus de move pour les 2 joueurs
# la fonction retourne true

# Sinon elle retourne false


	if len(board[0])+len(board[1]) == 64:
		return True

	elif len (AIStrat.movePossibles(board)[0]) == 0 and (AIStrat.movePossibles([board[1],board[0]])[0]) == 0:
		return True 

	else:
		return False

def utility (board):
# Fonction qui retourne 1 si le nombre de pions de notre joueur est plus grand que celui de l'adversaire
# Sinon elle retourne -1

	if len (board[0]) > len (board[1]):
		return 1

	else: 
		return -1


def heuristic(board):

# Fonction heuristique
# .... À compléter 

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
# Fonction qui retourne la stratégie choisie

	return MIN(board)[1]



#print(Strat([[28, 35],[27, 36]]))

print(Strat([[8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61],
		[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
		45, 46, 49, 50, 53, 54, 55, 62, 63]]))
print(Strat([[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
		45, 46, 49, 50, 53, 54, 55, 62, 63],[8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61],
		]))









	





