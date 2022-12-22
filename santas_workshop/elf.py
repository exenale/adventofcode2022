from santas_workshop.rugsack import Rugsack
class Elf():
    def __init__(self) -> None:
        pass
    
    def give_rugsack(self, rugsack: Rugsack):
        self.rugsack = rugsack
    
    def change_group_setting(self, has_group):
        self.has_group = has_group
    
    def give_food(self, food_list):
        self.food_list = food_list
        self.total_calories = self.total_calories()
    
    def total_calories(self):
        total_cal = 0
        for food in self.food_list.splitlines():
            total_cal = total_cal+int(food.strip())
        return total_cal