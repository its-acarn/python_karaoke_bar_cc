import unittest
from src.guests import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.jack = Guest("Jack", 100.00)

    def test_guest_exists(self):
        self.assertEqual("Jack", self.jack.name)
        self.assertEqual(100.00, self.jack.money)