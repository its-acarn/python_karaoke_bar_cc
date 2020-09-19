class Room:

    def __init__(self, name, guest_limit):
        self.name = name
        self.guest_limit = guest_limit
        self.cash = 0
        self.current_guests = []

    def guest_check_in(self, room, guest):
        room.current_guests.append(guest)