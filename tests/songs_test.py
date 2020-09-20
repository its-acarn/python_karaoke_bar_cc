import unittest
from src.songs import Song
from src.rooms import Room

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("S Club 7", "Reach")
        self.song_2 = Song("Bob Dylan", "Blowin' in the Wind")
        self.room_1 = Room("Tokyo", 3)


    def test_song_exists(self):
        self.assertEqual("S Club 7", self.song_1.artist)
        self.assertEqual("Reach", self.song_1.name)
        self.assertEqual(False, self.song_1.is_playing)


    def test_song_status_changes(self):
        self.room_1.add_song_to_room(self.song_1)
        self.song_1.change_song_status(self.room_1)
        self.song_2.change_song_status(self.room_1)
        self.assertEqual(True, self.song_1.is_playing)
        self.assertEqual(False, self.song_2.is_playing)

        self.room_1.add_song_to_room(self.song_2)
        self.song_1.change_song_status(self.room_1)
        self.song_2.change_song_status(self.room_1)
        self.assertEqual(False, self.song_1.is_playing)
        self.assertEqual(True, self.song_2.is_playing)
        
        