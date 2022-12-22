
import string
import sys
sys.path.append('/Users/jasmine/Repos/advent_of_code_2022/')

from santas_workshop.rugsack import Rugsack
from santas_workshop.elf_group import ElfGroup
from santas_workshop.elf import Elf


def main():
    f = open("3/input.txt", "r")
    input_text = f.read()
    rugsacks = []
    total_priority = 0

    #ANSWER ONE
    for lin in input_text.splitlines():
        rugsack = Rugsack(lin)
        rugsacks.append(rugsack)
        total_priority += rugsack.add_common_item_priorities()
    print(total_priority)

    #ANSWER TWO
    elf_groups = []
    last_group = ElfGroup()
    elf_groups.append(last_group)
    for rugsack in rugsacks:
        new_elf = Elf()
        new_elf.give_rugsack(rugsack)
        if not last_group.add_elf(new_elf):
            last_group = ElfGroup()
            last_group.add_elf(new_elf)
            elf_groups.append(last_group)

    sum_emblems = 0
    for elf_group in elf_groups:
        elf_group.find_group_emblem()
        sum_emblems += elf_group.group_emblem_value
    print(sum_emblems)






main()