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
    
    def test_guest_in_room(self):
        self.room_1.guest_check_in(self.jack)
        self.jack.guest_in_room(self.room_1)
        self.assertEqual(self.room_1, self.jack.current_room)
        # print(self.room_1.current_guests[0].name)