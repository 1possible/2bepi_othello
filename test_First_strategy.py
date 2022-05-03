import First_strategy

def test_apply():
    plateauSuccesseur = First_strategy.apply([44,1], [[28, 35], [27, 36]])
    assert set(plateauSuccesseur[0]) == {28,35,36,44} and set(plateauSuccesseur[1]) =={27}

def test_gameOver ():
    assert First_strategy.gameOver(
        [[0,8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61],
         [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
          45, 46, 49, 50, 53, 54, 55, 62, 63]]) == True

    assert First_strategy.gameOver([[28, 35],[27, 36]]) == False

