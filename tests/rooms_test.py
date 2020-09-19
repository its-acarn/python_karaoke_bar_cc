import unittest
from src.rooms import Room
from src.guests import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Tokyo", 8)
        self.jack = Guest("Jack", 100.00)
        self.kalvin = Guest("Kalvin", 100.00)

    def test_room_exists(self):
        self.assertEqual("Tokyo", self.room_1.name)
        self.assertEqual(8, self.room_1.guest_limit)
        self.assertEqual(0, self.room_1.cash)
        self.assertEqual(0, len(self.room_1.current_guests))

    def test_guest_check_in(self):
        self.room_1.guest_check_in(self.room_1, self.jack)
        self.room_1.guest_check_in(self.room_1, self.kalvin)
        self.assertEqual(2, len(self.room_1.current_guests))

    def test_guest_check_out(self):
        self.room_1.guest_check_in(self.room_1, self.jack)
        self.room_1.guest_check_in(self.room_1, self.kalvin)

        self.room_1.guest_check_out(self.room_1, self.jack)
        self.assertEqual(1, len(self.room_1.current_guests))

    def test_guest_limit_not_exceeded(self):
        self.room_1.guest_check_in(self.room_1, self.jack)
        self.room_1.guest_check_in(self.room_1, self.kalvin)
        G3 = Guest("Luke", 100.00)
        self.room_1.guest_check_in(self.room_1, G3)
        G4 = Guest("Liam", 100.00)
        self.room_1.guest_check_in(self.room_1, G4)
        G5 = Guest("Stuart", 100.00)
        self.room_1.guest_check_in(self.room_1, G5)
        G6 = Guest("Patrick", 100.00)
        self.room_1.guest_check_in(self.room_1, G6)
        G7 = Guest("Marcelo", 100.00)
        self.room_1.guest_check_in(self.room_1, G7)
        G8 = Guest("Helder", 100.00)
        self.room_1.guest_check_in(self.room_1, G8)
        G9 = Guest("Robin", 100.00)
        self.room_1.guest_check_in(self.room_1, G9)
        

        self.assertEqual(8, len(self.room_1.current_guests))
