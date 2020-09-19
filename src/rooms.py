class Room:

    def __init__(self, name, guest_limit):
        self.name = name
        self.guest_limit = guest_limit
        self.cash = 0
        self.current_guests = []

    def guest_check_in(self, room, guest):
        if len(room.current_guests) >= room.guest_limit:
            return f"Sorry {guest.name}, the room {room.name} is currently full."
        else:
            room.current_guests.append(guest)

    def guest_check_out(self, room, guest):
        room.current_guests.remove(guest)

    # def guest_limit_check(self, room, guest):
       
