import unittest
from app.models.game import *
from app.models.player import *

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.player_1 = Player('Robert', 'rock')
        self.player_2 = Player('Philippa', 'paper')
        self.player_3 = Player('Siobhan', 'scissors')


    def test_player_1_win(self):
        winner = self.game.check_winner(self.player_1, self.player_3)
        self.assertEqual(self.player_1, winner)
