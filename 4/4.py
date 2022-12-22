from santas_workshop import elf


def does_area_one_contain_area_two (area_one, area_two):
    one_start, one_end = [int(x) for x in area_one.split("-")]
    two_start, two_end = [int(x) for x in area_two.split("-")]

    if two_start>= one_start and two_start <= one_end:
        # print(one_start, one_end, two_start, two_end)
        if two_end>= one_start and two_end <= one_end:
            return True
    return False


def any_overlap (area_one, area_two):
    one_start, one_end = [int(x) for x in area_one.split("-")]
    two_start, two_end = [int(x) for x in area_two.split("-")]
    if two_start>= one_start and two_start <= one_end:
        return True
    if two_end>= one_start and two_end <= one_end:
        return True
    return False


f = open("4/input.txt", "r")
input_text = f.read()
rugsacks = []
total_priority = 0
count_pairs = 0
count_pairs_two = 0
#ANSWER ONE
for lin in input_text.splitlines():
    elf_one_area, elf_two_area = lin.split(",")

    if does_area_one_contain_area_two(elf_one_area, elf_two_area) or does_area_one_contain_area_two(elf_two_area, elf_one_area):
        count_pairs += 1
    if any_overlap(elf_one_area, elf_two_area) or any_overlap(elf_two_area, elf_one_area):
        count_pairs_two += 1

print(count_pairs)
print(count_pairs_two)