import unittest

from classes.guests import Guests


class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guests = Guests("Mary", 10)

    def test_guest_has_name(self):
        self.assertEqual("Mary", self.guests.name)

    def test_guest_has_money(self):
        self.assertEqual(10, self.guests.money)
