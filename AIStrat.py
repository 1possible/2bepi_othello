import random

directionList = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
def changeStyleMove(listMove):
    if len(listMove)>0:
        nLmove = [[],[]]
        for move in listMove:
            nLmove[0].append(move[0])
            nLmove[1].append(move[1])
        return nLmove
    else:
        return []


def movePossibles(board):
    #fonction qui renvoie dans une liste tout les moves possible à faire avec cette ce plateau
    #Parametre:
    #   board: list a 2 élément
    #           board[0]: liste qui contient les cases de ses pieces
    #           board[1]: liste qui contient les cases des piece de son adversaire
    #return:
    #   une liste des moves
    #       les moves possible sont sous forme de liste à 2 éléments
    #           l'élément 0: int: la case du move
    #           l'élément 1: int: le nombre de piece prise avec ce move
    movesList = []
    for pion in board[0]:
        for direction in directionList:
            isACoup = coup(pion,direction,board)
            if isACoup is not None:
                movesList = moveInMovesList(movesList,isACoup)
    return movesList

def moveInMovesList(movesList,newMove):
    #rajoute un move a une liste de moves
    # en prenant en compte si il y a une autre move sur la même case
    # dans ce cas il rajoute les points  du newMove a celui existant
    #Parametre:
    #   movesList: liste de move
    #   newMove : un move que l'on veut rajouté dans movesList
    #
    #       les moves sont sous forme de liste à 2 élément
    #           le element 0: int: la case du move
    #           le element 1: int :le nombre de piece prise avec ce move
    #Return :
    #   movesList avec le nouveau move rajouté

    isAmoveDouble = False
    for i in range(len(movesList)):
        if newMove[0] == movesList[i][0]:
            isAmoveDouble = True
            movesList[i][1] += newMove[1]
    if(isAmoveDouble)== False:
        movesList.append(newMove)
    return movesList


def coup(case, direction, board, point =0):
    # fonction récursive qui cherche s'il y a un move possible avec le pion sur la CASE et dans la DIRECTION
    # (qui est en parametre)
    #Parametre:
    #   case        : int compris entre 0 et 63 inclus: case du pion que l'on veut regarder
    #   direction   : direction par rapport à la CASE du pion que l'on va vérifier pour voir si il y a un move
    #                 tuple avec comme premier élément -1,0,1 qui fait reference à la colonne
    #                                  deuxieme élément -1,0,1 qui fait référence à la ligne
    #   board       : l'etat du plateau sour forme de list à 2 éléments
    #                       board[0] :liste qui contient les cases de ses pieces
    #                       board[1] : liste qui contient les cases des piece de son adversaire
    #   point       : Int: nombre de point aquis par le mouvement (sert lors de la recusivité)
    #Return:
    #   si il y a pas de move possible dans la direction renvoie None
    #   sinon renvoie le move sont sous forme de liste à 2 élément
    #                le element 0: int :la case du move
    #                le element 1: int :le nombre de piece prise avec ce move
    caseRech = (caseDacote(case,direction))
    if caseRech is None:
        return None
    elif(caseRech in board[1]):
        return coup(caseRech,direction, board, point+1)
    elif(caseRech in board[0]):
        return None
    else:
        if point == 0 :
            return None
        else:
            return [caseRech, point]
    #(caseMove , pience prise)

def caseDacote(case, direction):
    # revoie la case qui se trouve à coté dans la DIRECTION
    # Parametre:
    #   case        : int compris entre 0 et 63 inclus: case de référence
    #   direction   : tuple avec comme premier élément -1,0,1 qui fait reference à la colonne
    #                                  deuxiemme élément -1,0,1 qui fait référence à la ligne
    #Return:
    #   si la case demande se trouve en dehors des limite du plateau
    #       None
    #   sinon
    #       int: numeros de la case à coté de la case(en paramètre) dans la direction donnée
    c = case%8
    l = case//8
    if ((c == 0 and direction[0]==-1) or (c==7 and direction[0] == 1)):
        return None
    elif ((l == 0 and direction[1]==-1) or (l==7 and direction[1] == 1)):
        return None
    else :
        return (l + direction[1])*8 + c+direction[0]

def moveWithMaxPoint(listMove):
    #renvoie la place dans la listMove du coup avec le plus de point
    #Parametre:
    #   listMove: une liste des moves
    #           les moves possible sont sous forme de liste à 2 éléments
    #               l'élément 0: int: la case du move
    #               l'élément 1: int: le nombre de piece prise avec ce move
    #Return:
    #   si liste est vide
    #       None
    #   Sinon
    #       int: place dans la listMove du coup avec le plus de point
    placeMoveInList = None
    for i in range(len(listMove)):
        if placeMoveInList is None:
            placeMoveInList = i
        else:
            if listMove[i][1]>listMove[placeMoveInList][1]:
                placeMoveInList = i
    return placeMoveInList

def moveWithMinPoint(listMove):
    #renvoie la place dans la listMove du coup avec le moins de point
    #Parametre:
    #   listMove: une liste des moves
    #           les moves possible sont sous forme de liste à 2 éléments
    #               l'élément 0: int: la case du move
    #               l'élément 1: int: le nombre de piece prise avec ce move
    #Return:
    #   si liste est vide
    #       None
    #   Sinon
    #       int: place dans la listMove du coup avec le moins de point
    placeMoveInList = None
    for i in range(len(listMove)):
        if placeMoveInList is None:
            placeMoveInList = i
        else:
            if listMove[i][1]<listMove[placeMoveInList][1]:
                placeMoveInList = i
    return placeMoveInList
def strategieDuMoinsDePion(board):
    moveList = movePossibles(board)
    if len(moveList) >0:
        nMoveList = changeStyleMove(moveList)
        if 0 in nMoveList[0]:
            return 0
        elif 7 in nMoveList[0]:
            return 7
        elif 56 in nMoveList[0]:
            return 56
        elif 63 in nMoveList[0]:
            return 63
        elif (len(board[0])+len(board[1]))<= 50:
            return nMoveList[0][moveWithMinPoint(moveList)]
        else:
            return nMoveList[0][moveWithMaxPoint(moveList)]
    else:
        return None
def bestCoupInThemoment(board):
    #renvoie la case du move qui rapport le plus de point dans les coups possible ce tour ci (ne prend rien d'autre en compte)
    #Parametre:
    #   board: list a 2 élément
    #           board[0]:liste qui contient les cases de ses pieces
    #           board[1]:liste qui contient les cases des piece de son adversaire
    # Return:
    #   si il n'y a pas de mouvement possible
    #       None
    #   sinon
    #       int: chiffre de 0 à 63 correspondant une case du move qui rapport le plus de point

    moveList = movePossibles(board)
    placeMoveInList = moveWithMaxPoint(moveList)
    if placeMoveInList == None:
        return placeMoveInList
    else:
        return moveList[placeMoveInList][0]

def aleatoireCoup(board):
    #renvoie la case d'un move aléatoire dans tout ceux disponible
    #Parametre:
    #   board: list a 2 élément
    #           board[0]:liste qui contient les cases de ses pieces
    #           board[1]:liste qui contient les cases des piece de son adversaire
    #Return:
    #   si il n'y a pas de mouvement possible
    #       None
    #   sinon
    #       int: chiffre de 0 à 63 correspondant une case d'un move possible

    movesList = movePossibles(board)
    if len(movesList) == 0:
        return None
    else:
        return random.choice(movesList)[0]