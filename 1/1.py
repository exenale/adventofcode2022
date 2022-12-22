class Elf():
    def __init__(self, food_list, elf_num):
        self.food_list = food_list
        self.total_calories = self.total_calories()
        self.elf_num = elf_num
    
    def total_calories(self):
        total_cal = 0
        for food in self.food_list.splitlines():
            total_cal = total_cal+int(food.strip())
        return total_cal


f = open("day1_input.txt", "r")
input_text = f.read()
f.close()
elf_data = input_text.split("\n\n")

elves = []
for idx, elf_list in enumerate(elf_data):
    new_elf = Elf(elf_list, idx)
    elves.append(new_elf)

new_elf_list = elves
highest_cals = Elf("0", -1)
highest_cals2 = Elf("0", -1)
highest_cals3 = Elf("0", -1)
for elf in elves:
    if  elf.total_calories > highest_cals.total_calories:
        highest_cals = elf
new_elf_list.remove(highest_cals)
for elf in new_elf_list:
    if  elf.total_calories > highest_cals2.total_calories:
        highest_cals2 = elf
new_elf_list.remove(highest_cals2)
for elf in new_elf_list:
    if  elf.total_calories > highest_cals3.total_calories:
        highest_cals3 = elf

print(highest_cals.total_calories)
print(highest_cals2.total_calories)
print(highest_cals3.total_calories)

print(highest_cals.total_calories+highest_cals2.total_calories+highest_cals3.total_calories)