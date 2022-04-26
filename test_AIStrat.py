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