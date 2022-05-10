import AICom
def test_play():
    tCom = AICom.AICom(8101,"test","t")
    assert tCom.play({'request': 'play',
                      'lives': 3,
                      'errors': [],
                      'state': { 'players': ['test', 'dems']
                                ,'current': 0,
                                 'board': [[8, 16, 17, 20, 21, 24, 26, 32, 33, 34, 35, 36, 40, 42, 44, 47, 48, 51, 52, 56, 57, 58, 59, 60, 61],
         [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 25, 27, 28, 29, 30, 31, 37, 38, 39, 41, 43,
          45, 46, 49, 50, 53, 54, 55, 62, 63]]}}) == {"response": "move","move": 0,"message": "aleatoire"}