import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepo(unittest.TestCase):
    def test_init_player_set_attributes(self):
        r = PlayerRepository()
        self.assertEqual(len(r.players), 0)
        self.assertEqual(r.count, 0)

    def test_add_player(self):
        r = PlayerRepository()
        player = Advanced("Test")
        self.assertEqual(len(r.players), 0)
        self.assertEqual(r.count, 0)
        r.add(player)
        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)

    def test_add_existing_player_raises(self):
        r = PlayerRepository()
        player = Advanced("Test")
        self.assertEqual(len(r.players), 0)
        self.assertEqual(r.count, 0)
        r.add(player)
        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)
        with self.assertRaises(ValueError):
            r.add(player)
        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)

    def test_remove_player(self):
        r = PlayerRepository()
        player = Advanced("Test")
        self.assertEqual(len(r.players), 0)
        self.assertEqual(r.count, 0)
        r.add(player)
        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)
        r.remove(player.username)
        self.assertEqual(len(r.players), 0)
        self.assertEqual(r.count, 0)

    def test_remove_empty_player_raises(self):
        r = PlayerRepository()
        player = Advanced("Test")
        self.assertEqual(len(r.players), 0)
        self.assertEqual(r.count, 0)
        r.add(player)
        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)
        with self.assertRaises(ValueError):
            r.remove("")
        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)

    def test_find_a_player(self):
        r = PlayerRepository()
        player = Advanced("Test")
        self.assertEqual(len(r.players), 0)
        self.assertEqual(r.count, 0)
        r.add(player)
        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)
        self.assertEqual(r.find("Test"), player)

