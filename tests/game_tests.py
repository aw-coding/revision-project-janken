import unittest
from app.models.game import *
from app.models.player import *

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.player_1 = Player('Robert', 'rock')
        self.player_2 = Player('Philippa', 'paper')
        self.player_3 = Player('Siobhan', 'scissors')


    def test_player1_win(self):
        winner = self.game.check_winner(self.player_1, self.player_3)
        self.assertEqual(self.player_1, winner)

    def test_player2_can_win(self):
        winner = self.game.check_winner(self.player_2, self.player_1)
        self.assertEqual(self.player_2, winner)

    def test_draw(self):
        self.player_2.choice = 'rock'
        winner = self.game.check_winner(self.player_1, self.player_2)
        self.assertEqual(None, winner)