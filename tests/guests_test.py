import unittest
from src.guests import Guest
from src.rooms import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.jack = Guest("Jack", 100.00)
        self.room_1 = Room("Tokyo", 3)

    def test_guest_exists(self):
        self.assertEqual("Jack", self.jack.name)
        self.assertEqual(100.00, self.jack.money)
        self.assertEqual(None, self.jack.current_room)
    
    def test_guest_current_room(self):
        self.room_1.guest_check_in(self.jack)
        get_room = self.jack.find_guest_current_room(self.room_1)
        self.assertEqual(self.room_1, get_room)

        self.room_1.guest_check_out(self.jack)
        get_room = self.jack.find_guest_current_room(self.room_1)
        self.assertEqual(None, get_room)