directionList = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]


def coup(case, direction, point ,board):
    caseRech = (caseDacote(case,direction))
    if(caseRech in board[1]):
        return coup(caseRech,direction, point+1,board)
    elif(caseRech in board[0]):
        return False
    else:
        if point == 0 :
            return False
        else:
            return [caseRech, point]
    #(caseMove , pience prise)

def caseDacote(case, direction):
    c = case%8
    l = case//8
    if ((c == 0 and direction[0]==-1) or (c==7 and direction[0] == 1)):
        return False
    elif ((l == 0 and direction[1]==-1) or (l==7 and direction[1] == 1)):
        return False
    else :
        return (l + direction[1])*8 + c+direction[0]