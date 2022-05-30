import unittest

from classes.rooms import Rooms
from classes.guests import Guests
from classes.songs import Songs


class TestRooms(unittest.TestCase):
    def setUp(self):
        self.rooms = Rooms("room1", 5)
        # self.playlist = Rooms.playlist("songs1", "artist1")

    def test_room_by_name(self):
        self.assertEqual("room1", self.rooms.name)

    def test_room_capacity(self):
        self.assertEqual(5, self.rooms.capacity)

    def test_room_has_no_guests(self):
        self.assertEqual(0, self.rooms.guests_in_room())

    def test_add_guest(self):
        guest = Guests("Mary", 10)
        self.rooms.add_guest(guest)
        self.assertEqual(1, self.rooms.guests_in_room())

    def test_remove_guest(self):
        guest = Guests("Mary", 10)
        self.rooms.add_guest(guest)
        self.rooms.remove_guest(guest)
        self.assertEqual(0, self.rooms.guests_in_room())

    def test_is_playlist_empty(self):
        self.assertEqual(0, self.rooms.check_playlist())

    # def test_add_song_to_playlist(self):
    #     song_to_add = Songs("song1", "artist1")
    #     self.rooms.add_song_to_playlist(song_to_add)
    #     self.assertEqual(("songs1"), self.rooms.playlist)
