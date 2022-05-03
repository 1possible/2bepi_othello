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


def test_utility():

	assert First_strategy.utility ([[0,8,16,24,32,40,48,56,57,58,59,60,61,62,63,9,17,25,33,41,49,18,27,36,45,54,63,61,52,43,34],
	[2,3,4,5,6,7,10,11,12,13,14,15,19,20,21,22,23,28,29,30,31,26,37,38,39,35,46,47,44,42,55,53,50,51]]) == -1
