class Guest:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.current_room = None

    # potential to add to guest check in/out functions
    def find_guest_current_room(self, room):
        guest_found = False
        for guest in room.current_guests:
            if self == guest:
                self.current_room = room
                guest_found = True
        
        if guest_found == False:
            self.current_room = None

        return self.current_room
                
        
        
        
    

    