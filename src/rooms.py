class Room:

    def __init__(self, name, guest_limit):
        self.name = name
        self.guest_limit = guest_limit
        self.cash = 0
        self.entry_price = 10.00
        self.current_guests = []
        self.current_song = None
        self.recently_played = []
        self.last_played = None


    def add_song_to_room(self, song):
        if self.current_song != None:
            self.recently_played.append(self.current_song)
        
        self.current_song = song
    

    def find_last_played(self):
        if self.recently_played != []:
            self.last_played = self.recently_played[-1]


    def add_guest_to_room(self, guest):
        if len(self.current_guests) >= self.guest_limit:
            return f"Sorry {guest.name}, the room {self.name} is currently full."
        else:
            self.current_guests.append(guest)


    def remove_guest_from_room(self, guest):
        self.current_guests.remove(guest)
        guest.current_room = None


    def take_entry_price_from_guest(self, guest):
        if guest.money >= self.entry_price:
            self.cash += self.entry_price
        else:
            return "You do not have enough money to enter this room."


    def guest_check_in(self, guest):
        self.add_guest_to_room(guest)
        self.take_entry_price_from_guest(guest)
        guest.pay_to_enter_room(self)
        guest.current_room = self
        

    def guest_check_out(self, guest):
        self.remove_guest_from_room(guest)

