import First_strategy

def test_apply():
    plateauSuccesseur = First_strategy.apply(44, [[28, 35], [27, 36]])
    assert set(plateauSuccesseur[0]) == {28,35,36,44} and set(plateauSuccesseur[1]) =={27}