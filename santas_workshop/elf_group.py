from santas_workshop.elf import Elf
from santas_workshop.rugsack import get_letter_value

class ElfGroup():
    def __init__(self) -> None:
        self.elf_list = []
        self.limit_elves = 3
        pass

    def add_elf(self, elf: Elf):
        if len(self.elf_list) < self.limit_elves:
            self.elf_list.append(elf)
            elf.change_group_setting(has_group=True)
            return True
        return False
    
    def find_group_emblem(self):
        for letter in self.elf_list[0].rugsack.whole_sack:
            if self.is_in_both_rugsacks(letter, self.elf_list[1], self.elf_list[2]):
                self.group_emblem = letter
                self.group_emblem_value = get_letter_value(letter)
    
    def is_in_both_rugsacks(self, item:str, elf_1, elf_2):
        if elf_1.rugsack.whole_sack.find(item) > -1 and elf_2.rugsack.whole_sack.find(item)  > -1:
            return True
        return False
