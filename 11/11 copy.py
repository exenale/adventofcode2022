import math
op = {'+': lambda x, y: x + y,
      '*': lambda x, y: x * y}
class Item():
    def __init__(self, worry) -> None:
        self.worry_level = worry
    
    def change_worry_level(self, new_level):
        self.worry_level = new_level
    
    def bored_worry_level(self):
        new_level = self.worry_level/3
        self.worry_level = math.trunc(new_level)

class Monkey():
    def __init__(self, lines) -> None:
        self.parse_monkey(lines)
        self.inspected_items = 0

    def parse_monkey(self, monkey_desc):

        lines = monkey_desc
        self.monkey_num = lines[0].split()[1].replace(":", "")
        self.create_worry_change_function(lines[2])
        self.collect_starting_items(lines[1])
        self.divisor_num = int(lines[3].split()[3])
        self.true_monkey_num = lines[4].split()[5]
        self.false_monkey_num = lines[5].split()[5]

    def set_throwing_monkeys(self, monkey_list):
        lcm = 1
        for monkey in monkey_list:
            if monkey.monkey_num == self.true_monkey_num:
                self.true_monkey = monkey
            if monkey.monkey_num == self.false_monkey_num:
                self.false_monkey = monkey
            lcm = lcm * monkey.divisor_num
        self.lcm = lcm
        

    def catch_item(self, item):
        self.items.append(item)

    def throw_item(self, worry_level, item):
        if worry_level % self.divisor_num == 0:
            self.true_monkey.catch_item(item)
        else:
            self.false_monkey.catch_item(item)
        
    
    def run_round(self):
        for item in self.items:
            new_worry_level = self.worry_change_op(item.worry_level)
            
            item.change_worry_level(new_worry_level%self.lcm)
            self.inspected_items +=1
            # item.bored_worry_level()
            self.throw_item(new_worry_level, item)
        self.items = []

    def print_item_worry(self):
        worry_levels =[]
        for item in self.items:
            worry_levels.append(item.worry_level)
        print(worry_levels)



    def collect_starting_items(self, line):
        items = line.split()[2:len(line.split())]
        new_items = []
        for item  in items:
            new_item = Item(int(item.replace(",", "")))
            new_items.append(new_item)
        self.items = new_items


    def create_worry_change_function(self, worry_change):
        worry_words = worry_change.split()
        self.operation = worry_words[4]
        self.second_value = worry_words[5]

    def worry_change_op(self, old_worry):
        if self.second_value== "old":
            return op[self.operation](old_worry, old_worry)
        second_value = int(self.second_value)
        return op[self.operation](old_worry, second_value)





f = open("11/input.txt", "r")
input_text = f.read()
input_lines = input_text.splitlines()
num_of_monkeys = 7
num_of_rounds = 10000
monkey_list = []
for i in range(0,num_of_monkeys+1):
    monkey = Monkey(input_lines[i*7:7+i*7])
    monkey_list.append(monkey)



for monkey in monkey_list:
    monkey.set_throwing_monkeys(monkey_list)


for i in range(0, num_of_rounds):
    for monkey in monkey_list:
        monkey.run_round()
    print(f"Round {i+1} has finished")

num_list = []
for monkey in monkey_list:
    num_list.append(monkey.inspected_items)
    print(f"Monkey {monkey.monkey_num} threw {monkey.inspected_items} times")

num_list.sort(reverse=True)
print(num_list[0]*num_list[1])