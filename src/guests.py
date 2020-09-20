class Guest:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.current_room = None

    def guest_in_room(self, room):
        for guest in room.current_guests:
            if self == guest:
                self.current_room = room
        
        
    

    