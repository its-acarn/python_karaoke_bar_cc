import unittest
from src.songs import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Bob Dylan", "Blowin' in the Wind", 234.00)

    def test_song_exists(self):
        self.assertEqual("Bob Dylan", self.song_1.artist)
        self.assertEqual("Blowin' in the Wind", self.song_1.name)
        self.assertEqual(234.00, self.song_1.length)
        self.assertEqual(False, self.song_1.is_playing)