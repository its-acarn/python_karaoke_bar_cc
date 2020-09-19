import unittest
from src.songs import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Bob Dylan", "Blowin' in the Wind", 234.00)

    def test_song_has_artist(self):
        self.assertEqual("Bob Dylan", self.song_1.artist)