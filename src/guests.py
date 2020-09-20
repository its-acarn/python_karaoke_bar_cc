class Guest:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.current_room = None

    # potential to add to guest check in/out functions
    def update_guest_current_room(self, room):
        for guest in room.current_guests:
            if self == guest:
                self.current_room = room
                
    def pay_to_enter_room(self, room):
        if self.money >= room.entry_price:
            self.money -= room.entry_price
        else:
            return "Not enough money."

        
        
    

    