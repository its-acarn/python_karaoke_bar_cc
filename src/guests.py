class Guest:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.current_room = None

                
    def pay_to_enter_room(self, room):
        if self.money >= room.entry_price:
            self.money -= room.entry_price
        else:
            return "Not enough money."

        
        
    

    