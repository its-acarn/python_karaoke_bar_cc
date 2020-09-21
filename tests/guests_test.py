import unittest
from src.guests import Guest
from src.rooms import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.jack = Guest("Jack", 100.00)
        self.kalvin = Guest("Kalvin", 5.00)
        self.room_1 = Room("Tokyo", 3)


    def test_guest_exists(self):
        self.assertEqual("Jack", self.jack.name)
        self.assertEqual(100.00, self.jack.money)
        self.assertEqual(None, self.jack.current_room)


    def test_pay_to_enter_room(self):
        self.jack.pay_to_enter_room(self.room_1)
        self.assertEqual(90, self.jack.money)

    def test_pay_to_enter_room__reject(self):
        get = self.kalvin.pay_to_enter_room(self.room_1)
        self.assertEqual("Not enough money.", get)