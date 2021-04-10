import unittest

from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestController(unittest.TestCase):
    def test_init_controller(self):
        c = Controller()
        self.assertEqual(len(c.player_repository.players), 0)
        self.assertEqual(len(c.card_repository.cards), 0)

    def test_add_players_success(self):
        c = Controller()
        res1 = c.add_player("Beginner", "testbeginner")
        res2 = c.add_player("Advanced", "testadvanced")
        self.assertEqual(res1,"Successfully added player of type Beginner with username: testbeginner")
        self.assertEqual(res2,"Successfully added player of type Advanced with username: testadvanced")

    def test_add_cards_success(self):
        c = Controller()
        res1 = c.add_card("Magic", "testcard")
        res2 = c.add_card("Trap", "testcard2")
        self.assertEqual(res1,"Successfully added card of type MAgicCard with name: testcard")
        self.assertEqual(res2,"Successfully added card of type TrapCard with name: testcard2")
