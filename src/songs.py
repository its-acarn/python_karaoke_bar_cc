class Song:
    
    def __init__(self, artist, name):
        self.artist = artist
        self.name = name
        self.is_playing = False

    def change_song_status(self, room):
        if self == room.current_song:
            self.is_playing = True

        else:
            self.is_playing = False