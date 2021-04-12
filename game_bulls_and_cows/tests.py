import unittest

from player import Player


class TestPlayer(unittest.TestCase):
    def test_player_initialization(self):
        p = Player("Testplayer", 1234)
        self.assertEqual(p.name, "Testplayer")
        self.assertEqual(p.secret_num, 1234)
        self.assertGreater(len(p.possible_opponent_nums), 100)
        self.assertTrue(1234 in p.possible_opponent_nums)
        self.assertFalse(2234 in p.possible_opponent_nums)

    def test_player_initialization_with_no_secret_num(self):
        p = Player("Testplayer")
        print(p.possible_opponent_nums)
        # self.assertEqual(len(p.secret_num), 4)
        self.assertTrue(p.is_valid_number(p.secret_num))

    def test_is_valid_number(self):
        self.assertTrue(Player.is_valid_number(1234))
        self.assertTrue(Player.is_valid_number(9874))
        self.assertFalse(Player.is_valid_number(2269))
        self.assertFalse(Player.is_valid_number(9429))