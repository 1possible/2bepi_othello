import random

directionList = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
def movePossibles(board):
    #ATTENTION: bad move
    #board[0] contient ses pieces
    #board[1] contient les piece de sont adversaire
    #return une list
    #       contenant les coup possible sous forme de list: comme
    #           le element 0: la case du move
    #           le element 1: le nombre de piece prise avec ce coup
    movesList = []
    for pion in board[0]:
        for direction in directionList:
            isACoup = coup(pion,direction,0,board)
            if isACoup is not None:
                movesList = moveInMovesList(movesList,isACoup)
    return movesList

def moveInMovesList(movesList,move):
    isAmoveDouble = False
    for i in range(len(movesList)):
        if move[0] == movesList[i][0]:
            isAmoveDouble = True
            movesList[i][1] += move[1]
    if(isAmoveDouble)== False:
        movesList.append(move)
    return movesList


def coup(case, direction, point ,board):
    # problem avec la iteration depasse la limite de python (plus que 100)
    caseRech = (caseDacote(case,direction))
    if caseRech is None:
        return None
    elif(caseRech in board[1]):
        return coup(caseRech,direction, point+1,board)
    elif(caseRech in board[0]):
        return None
    else:
        if point == 0 :
            return None
        else:
            return [caseRech, point]
    #(caseMove , pience prise)

def caseDacote(case, direction):
    c = case%8
    l = case//8
    if ((c == 0 and direction[0]==-1) or (c==7 and direction[0] == 1)):
        return None
    elif ((l == 0 and direction[1]==-1) or (l==7 and direction[1] == 1)):
        return None
    else :
        return (l + direction[1])*8 + c+direction[0]

def aleatoireCoup(board):
    movesList = movePossibles(board)
    if len(movesList) == 0:
        return None
    else:
        return random.choice(movesList)[0]