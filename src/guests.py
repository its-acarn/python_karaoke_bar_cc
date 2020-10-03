class Guest:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.current_room = None

                
    def pay_to_enter_room(self, room_cost):
        if self.money >= room_cost:
            self.money -= room_cost
        else:
            return "Not enough money."

        
        
    

    