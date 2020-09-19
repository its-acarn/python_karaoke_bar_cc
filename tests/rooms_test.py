import unittest
from src.rooms import Room
from src.guests import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Tokyo", 3)
        self.jack = Guest("Jack", 100.00)
        self.kalvin = Guest("Kalvin", 100.00)

    def test_room_exists(self):
        self.assertEqual("Tokyo", self.room_1.name)
        self.assertEqual(3, self.room_1.guest_limit)
        self.assertEqual(0, self.room_1.cash)
        self.assertEqual(0, len(self.room_1.current_guests))

    def test_guest_check_in(self):
        self.room_1.guest_check_in(self.jack)
        self.room_1.guest_check_in(self.kalvin)
        self.assertEqual(2, len(self.room_1.current_guests))

    def test_guest_check_out(self):
        self.room_1.guest_check_in(self.jack)
        self.room_1.guest_check_in(self.kalvin)

        self.room_1.guest_check_out(self.jack)
        self.assertEqual(1, len(self.room_1.current_guests))

    def test_guest_limit_not_exceeded(self):
        self.room_1.guest_check_in(self.jack)
        self.room_1.guest_check_in(self.kalvin)
        stuart = Guest("stuart", 100.00)
        self.room_1.guest_check_in(stuart)
        liam = Guest("Liam", 100.00)
        self.room_1.guest_check_in(liam)
        

        self.assertEqual(3, len(self.room_1.current_guests))
