import unittest
from app.models.player import *

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player('Robert', 'rock')
        self.player_2 = Player('Philippa', 'paper')
        self.player_3 = Player('Siobhan', 'scissors')


    def test_player_has_name(self):
        self.assertEqual('Robert', self.player_1.name)

    def test_player_has_choice(self):
        self.assertEqual('rock', self.player_1.choice)
