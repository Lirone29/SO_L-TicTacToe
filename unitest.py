import unittest
import  ticTacToe



class MyTest(unittest.TestCase):

    def setUp(self):
        self.lst = ['1','2','4']

    def test_does_player_win(self):
        #board = #gdzie player wygrywa
        self.assertTrue(ticTacToe.does_player_win("O", board))

    def test_in_two(self):
        self.assertIn('1', self.lst)

if __name__ == '__main__':
    unittest.main()