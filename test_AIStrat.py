import AIStrat

def test_caseDacote():
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    caseAcotede27 =[35,19,28,26,36,18,34,20]
    for i in range(8):
        assert AIStrat.caseDacote(27,direction[i]) == caseAcotede27[i]
    assert AIStrat.caseDacote(5,(0,-1)) == False
    assert AIStrat.caseDacote(23, (1, 1)) == False
    assert AIStrat.caseDacote(40, (-1, 1)) == False
    assert AIStrat.caseDacote(60, (0, 1)) == False

def test_coup():
    assert AIStrat.coup(28,(-1,0),0,[[28, 35],[27, 36]]) == [26,1]
    assert AIStrat.coup(28, (1, 0), 0, [[28, 35], [27, 36]]) == False
    assert AIStrat.coup(36,(-1,-1),0,[[26,28,36,44],[18,27,35,43]]) == [9,2]
    assert AIStrat.coup(28, (-1, 0), 0, [[26, 28, 36, 44], [18, 27, 35, 43]]) == False

def test_moveInMovesList():
    assert AIStrat.moveInMovesList([[9,3],[4,1],[20,2]],[9,1]) == [[9,4],[4,1],[20,2]]
    assert AIStrat.moveInMovesList([[9, 3], [4, 1], [20, 2]], [21, 3]) == [[9, 3], [4, 1], [20, 2],[21,3]]

def test_movePossibles():
    assert AIStrat.movePossibles([[28,35],[27,36]]) == [[44, 1], [26, 1], [19, 1], [37, 1]]