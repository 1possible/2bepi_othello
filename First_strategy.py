import AIStrat
from collections import defaultdict
import time
import asyncio

def timeit(fun):
	def wrapper(*args, **kwargs):
		start = time.time()
		res = fun(*args, **kwargs)
		print('Executed in {}s'.format(time.time() - start))
		return res
	return wrapper

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



def negamaxWithPruning(board,alpha=float('-inf'), beta=float('inf')):

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

def negamaxWithPruningLimitedDepth(board,depth=3,alpha=float('-inf'), beta=float('inf')):

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

class negamaxWithPruningIterativeDeepening:
	def __init__(self,timeout=4.45):
		self.cache = defaultdict(lambda: 0)
		self.score = 0
		self.move = None
		self.over = False
		self.start = time.time()
		self.depth =1
		self.timeout =timeout

	async def main(self,board):
		chrono =asyncio.create_task(self.search(board))
		await chrono
		return self.move

	async def search(self,board):
		searchperDepth = asyncio.create_task(self.threadNegamax(board))
		while not self.over:
			if time.time() - self.start >= self.timeout:
				break
			await asyncio.sleep(0)
		print("depth =", self.depth)


	async def cachedNegamaxWithPruningLimitedDepth(self,board, depth, alpha=float('-inf'), beta=float('inf')):
		over = gameOver(board)
		movesList = AIStrat.movePossibles(board)
		if over or depth==0:
			res = -heuristic(board), None, over
		else:
			meilleur_score, meilleur_coup,the_over = float('-inf'), None, True
			possiblility = [(move, apply(move,board))for move in movesList[0]]
			possiblility.sort(key=lambda poss: self.cache[(frozenset(poss[1][0]),frozenset(poss[1][1]))])
			for move, successor in reversed(possiblility):
				score, _ ,over= await self.cachedNegamaxWithPruningLimitedDepth([successor[1],successor[0]],depth-1,-beta, -alpha)
				await asyncio.sleep(0)
				the_over = the_over and over
				if score >= meilleur_score:
					meilleur_score, meilleur_coup = score, move
				alpha = max(alpha,meilleur_score)
				if alpha >=beta:
					break
			res = -meilleur_score,meilleur_coup, the_over
		self.cache[frozenset(board[0]),frozenset(board[1])] = res[0]
		return res
	async def threadNegamax(self,board):
		while self.score > float("-inf") and not self.over and time.time()-self.start < self.timeout-0.15:
			self.score, self.move, self.over = await self.cachedNegamaxWithPruningLimitedDepth(board, self.depth)
			self.depth += 1
			await asyncio.sleep(0)


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

	if len(board[0])+len(board[1]) <15:
		coefDifPion = 0
	elif len(board[0])+len(board[1]) <50:
		coefDifPion = 1
	elif len(board[0])+len(board[1]) <55:
		coefDifPion = 2
	else:
		coefDifPion = 4
	h += (len (board[0]) - len(board[1]))* coefDifPion
	pionIntouchable = 0
	for pion in board[0]:
		if(AIStrat.pionIntouchable(pion,board)):
			pionIntouchable+=1
	for pion in board[1]:
		if(AIStrat.pionIntouchable(pion,board)):
			pionIntouchable-=1
	h+=pionIntouchable
	h+= (len(AIStrat.movePossibles(board)[0])-len(AIStrat.movePossibles([board[1],board[0]])[0]))
	return h


@timeit
def StratIterative(board):
	search = negamaxWithPruningIterativeDeepening()
	return asyncio.run(search.main(board))


def Strat (board):
# Fonction qui retourne la stratégie choisie
	return negamaxWithPruningLimitedDepth(board)[1]



#print(StratIterative([[28, 35],[27, 36]]))

#print(StratIterative([[8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61],
#       [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
#          45, 46, 49, 50, 53, 54, 55, 62, 63]]))
#print(StratIterative([[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,#
#         45, 46, 49, 50, 53, 54, 55, 62, 63],[8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61],
#        ]))









	





