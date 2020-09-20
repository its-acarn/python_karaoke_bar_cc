import unittest
from src.rooms import Room
from src.guests import Guest
from src.songs import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Tokyo", 3)
        self.jack = Guest("Jack", 100.00)
        self.kalvin = Guest("Kalvin", 100.00)
        self.song_1 = Song("S Club 7", "Reach")


    def test_room_exists(self):
        self.assertEqual("Tokyo", self.room_1.name)
        self.assertEqual(3, self.room_1.guest_limit)
        self.assertEqual(0, self.room_1.cash)
        self.assertEqual(10.00, self.room_1.entry_price)
        self.assertEqual(0, len(self.room_1.current_guests))


    def test_guest_limit_not_exceeded(self):
        self.room_1.add_guest_to_room(self.jack)
        self.room_1.add_guest_to_room(self.kalvin)
        stuart = Guest("Stuart", 100.00)
        self.room_1.add_guest_to_room(stuart)
        liam = Guest("Liam", 100.00)
        self.room_1.add_guest_to_room(liam)
        
        self.assertEqual(3, len(self.room_1.current_guests))


    def test_add_song_to_room(self):
        self.room_1.add_song_to_room(self.song_1)
        self.assertEqual("S Club 7", self.room_1.current_song.artist)


    def test_add_song_to_room__recently_played(self):
        song_2 = Song("Bob Dylan", "Blowin' in the Wind")
        self.room_1.add_song_to_room(song_2)
        self.room_1.add_song_to_room(self.song_1)
        
        self.assertEqual("S Club 7", self.room_1.current_song.artist)
        self.assertEqual(1, len(self.room_1.recently_played))
        self.assertEqual("Bob Dylan", self.room_1.recently_played[0].artist)


    def test_find_last_played(self):
        self.assertEqual(None, self.room_1.last_played)
        self.room_1.add_song_to_room(self.song_1)
        song_2 = Song("Bob Dylan", "Blowin' in the Wind")
        self.room_1.add_song_to_room(song_2)
        self.room_1.find_last_played()
        self.assertEqual(self.song_1, self.room_1.last_played)


    def test_add_guest_to_room(self):
        self.room_1.add_guest_to_room(self.jack)
        self.room_1.add_guest_to_room(self.kalvin)
        self.assertEqual(2, len(self.room_1.current_guests))


    def test_remove_guest_from_room(self):
        self.room_1.guest_check_in(self.jack)
        self.room_1.guest_check_in(self.kalvin)

        self.room_1.remove_guest_from_room(self.jack)
        self.assertEqual(1, len(self.room_1.current_guests))


    def test_take_entry_price_from_guest(self):
        self.room_1.take_entry_price_from_guest(self.jack)
        self.assertEqual(10, self.room_1.cash)


    def test_guest_check_in(self):
        self.room_1.guest_check_in(self.jack)
        self.assertEqual(10.0, self.room_1.cash)
        self.assertEqual(90.0, self.jack.money)
        self.assertEqual(self.room_1, self.jack.current_room)
        self.assertEqual(1, len(self.room_1.current_guests))


    def test_guest_check_out(self):
        self.room_1.guest_check_in(self.jack)
        self.room_1.guest_check_in(self.kalvin)
        self.assertEqual(20.0, self.room_1.cash)
        self.assertEqual(90.0, self.jack.money)
        self.assertEqual(90.0, self.kalvin.money)
        self.assertEqual(self.room_1, self.jack.current_room)
        self.assertEqual(self.room_1, self.kalvin.current_room)
        self.assertEqual(2, len(self.room_1.current_guests))

        self.room_1.guest_check_out(self.jack)
        self.assertEqual(20.0, self.room_1.cash)
        self.assertEqual(None, self.jack.current_room)
        self.assertEqual(self.room_1, self.kalvin.current_room)
        self.assertEqual(1, len(self.room_1.current_guests))