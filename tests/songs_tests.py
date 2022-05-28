import unittest

from classes.songs import Songs
from classes.rooms import Rooms


class TestSongs(unittest.TestCase):
    def setUp(self):
        self.songs1 = Songs("song1", "artist1")
        self.songs2 = Songs("song2", "artist2")

    def test_get_song_by_name(self):
        self.assertEqual("song1", self.songs1.name)

    def test_find_artist_by_name(self):
        self.assertEqual("artist2", self.songs2.artist)
