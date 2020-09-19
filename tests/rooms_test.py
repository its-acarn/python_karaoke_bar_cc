import unittest
from src.rooms import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Tokyo", 8)

    def test_room_exists(self):
        self.assertEqual("Tokyo", self.room_1.name)
        self.assertEqual(8, self.room_1.guest_limit)
        self.assertEqual(0, len(self.room_1.current_guests))