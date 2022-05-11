import AIStrat

def test_caseDacote():
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    caseAcotede27 =[35,19,28,26,36,18,34,20]
    for i in range(8):
        assert AIStrat.caseDacote(27,direction[i]) == caseAcotede27[i]
    assert AIStrat.caseDacote(5,(0,-1)) is None
    assert AIStrat.caseDacote(23, (1, 1)) is None
    assert AIStrat.caseDacote(40, (-1, 1)) is None
    assert AIStrat.caseDacote(60, (0, 1)) is None

def test_coup():
    assert list(AIStrat.coup(28,(-1,0),[[28, 35],[27, 36]])) == [26,1]
    assert AIStrat.coup(28, (1, 0), [[28, 35], [27, 36]]) == (None,None)
    assert AIStrat.coup(36,(-1,-1),[[26,28,36,44],[18,27,35,43]]) == (9,2)
    assert AIStrat.coup(28, (-1, 0), [[26, 28, 36, 44], [18, 27, 35, 43]]) == (None,None)

def test_moveInMovesList():
    assert AIStrat.moveInMovesList([[9,4,20],[3, 1, 2]],9,1) == [[9,4,20],[4,1,2]]
    assert AIStrat.moveInMovesList([[9,4,20],[3, 1, 2]], 21, 3) == [[9,4,20,21],[3, 1, 2,3]]

def test_movePossibles():
    assert AIStrat.movePossibles([[28,35],[27,36]]) == [[44,26,19,37],[ 1, 1, 1, 1]]
    assert AIStrat.movePossibles([[10,11,17,20,22,25,28,30,33,34,36,37,38,41,43,44,45,46,49,50,51,52,57,58],
                                  [0,1,2,3,5,8,9,12,16,18,19,26,27,32,35,40,42,48,53,56,59,62]]) == [[13,4,61,60,54],[ 1, 1, 1, 2, 1]]
    assert AIStrat.movePossibles([[8, 16,17,20,21,24,26,32,33,34,35,36,40,42,44,47,48,51,52,56,57,58,59,60,61],
                                  [1,2,3,4,5,6,7,9,10,11,12,13,14,15,18,19,22,23,25,27,28,29,30,31,37,38,39,41,43,45,46,49,50,53,54,55,62,63]])==[[0],[3]]
def test_moveWithMaxPoint():
    assert AIStrat.moveWithMaxPoint([[9,4,20],[4,1,2]]) == 0
    assert AIStrat.moveWithMaxPoint([[],[]]) is None

def test_moveWithMinPoint():
    assert AIStrat.moveWithMinPoint([[9,4,20],[4,1,2]]) == 1
    assert AIStrat.moveWithMinPoint([[],[]]) is None

def test_pionIntouchable():
    assert AIStrat.pionIntouchable(9,[[0,1,2,10,17],[]]) == False
    assert AIStrat.pionIntouchable(9, [[0, 1, 2,8], []]) == True
    assert AIStrat.pionIntouchable(54,[[63,62,61],[55]]) == False

def test_strategieDuMoinsDePion():
    assert AIStrat.strategieDuMoinsDePion([[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
          45, 46, 49, 50, 53, 54, 55, 62, 63],[8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61]]) == None
    assert AIStrat.strategieDuMoinsDePion([[8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61],
         [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
          45, 46, 49, 50, 53, 54, 55, 62, 63]]) == 0
    assert AIStrat.strategieDuMoinsDePion([[10, 11, 17, 20, 22, 25, 28, 30, 33, 34, 36, 37, 38, 41, 43, 44, 45, 46, 49, 50, 51, 52, 57, 58],
         [0, 1, 2, 3, 5, 8, 9, 12, 16, 18, 19, 26, 27, 32, 35, 40, 42, 48, 53, 56, 59, 62]]) in AIStrat.movePossibles([[10, 11, 17, 20, 22, 25, 28, 30, 33, 34, 36, 37, 38, 41, 43, 44, 45, 46, 49, 50, 51, 52, 57, 58],
         [0, 1, 2, 3, 5, 8, 9, 12, 16, 18, 19, 26, 27, 32, 35, 40, 42, 48, 53, 56, 59, 62]])[0]
    assert AIStrat.strategieDuMoinsDePion([[21],[6,14,15]]) == 7
    assert AIStrat.strategieDuMoinsDePion([[32], [6, 14,40,48,57,49]]) == 56
    assert AIStrat.strategieDuMoinsDePion([[61], [54,55,62]]) == 63
    assert AIStrat.strategieDuMoinsDePion([[29,36,7,15,23,47,55,63],[30,37,38]]) == 31
    assert AIStrat.strategieDuMoinsDePion([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                                           [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63]])== 59

def test_bestCoupInTheMoment():
    assert AIStrat.bestCoupInThemoment(
        [[10, 11, 17, 20, 22, 25, 28, 30, 33, 34, 36, 37, 38, 41, 43, 44, 45, 46, 49, 50, 51, 52, 57, 58],
         [0, 1, 2, 3, 5, 8, 9, 12, 16, 18, 19, 26, 27, 32, 35, 40, 42, 48, 53, 56, 59, 62]]) == 60

    assert AIStrat.bestCoupInThemoment(
        [[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
          45, 46, 49, 50, 53, 54, 55, 62, 63],
         [8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61],
         ]) is None

def test_aleatoireCoup():
    assert AIStrat.aleatoireCoup([[28, 35], [27, 36]]) in [44, 26, 19, 37]
    assert AIStrat.aleatoireCoup(
        [[8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61],
         [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
          45, 46, 49, 50, 53, 54, 55, 62, 63]]) == 0
    assert AIStrat.aleatoireCoup(
        [[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
          45, 46, 49, 50, 53, 54, 55, 62, 63],[8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61]
         ]) is None
