class Room:

    def __init__(self, name, guest_limit):
        self.name = name
        self.guest_limit = guest_limit
        self.cash = 0
        self.current_guests = []
        self.current_song = None
        self.recently_played = []

    def guest_check_in(self, guest):
        if len(self.current_guests) >= self.guest_limit:
            return f"Sorry {guest.name}, the room {self.name} is currently full."
        else:
            self.current_guests.append(guest)

    def guest_check_out(self, guest):
        self.current_guests.remove(guest)

    def add_song_to_room(self, song):
        if self.current_song != None:
            self.recently_played.append(self.current_song)
        
        self.current_song = song
       
