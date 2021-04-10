import unittest

from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository


class TestCardRepo(unittest.TestCase):
    def test_init_player_set_attributes(self):
        r = CardRepository()
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)

    def test_add_player(self):
        r = CardRepository()
        player = MagicCard("Test")
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)
        r.add(player)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

    def test_add_existing_player_raises(self):
        r = CardRepository()
        player = MagicCard("Test")
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)
        r.add(player)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)
        with self.assertRaises(ValueError):
            r.add(player)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

    def test_remove_player(self):
        r = CardRepository()
        player = MagicCard("Test")
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)
        r.add(player)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)
        r.remove(player.name)
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)

    def test_remove_empty_player_raises(self):
        r = CardRepository()
        player = MagicCard("Test")
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)
        r.add(player)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)
        with self.assertRaises(ValueError):
            r.remove("")
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

    def test_find_a_player(self):
        r = CardRepository()
        player = MagicCard("Test")
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)
        r.add(player)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)
        self.assertEqual(r.find("Test"), player)

