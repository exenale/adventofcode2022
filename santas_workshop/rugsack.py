import string
def get_letter_value(letter:str):
    alphabet_lower=string.ascii_lowercase  
    add_value = 1
    if letter.isupper():
        add_value = 27
    return alphabet_lower.find(letter.lower())+add_value

class Rugsack():
    def __init__(self, contents):
        half_size = int(len(contents)/2)
        self.whole_sack = contents
        self.compartment_1 = contents[0:half_size]
        self.compartment_2 = contents[half_size:len(contents)]

        self.alphabet_lower=string.ascii_lowercase      

    def add_common_item_priorities(self):
        total_val = 0
        letters_checked = []
        for letter in self.compartment_1:
            if(self.is_in_both_compartments(letter)) and letter not in letters_checked:
                letters_checked.append(letter)
                total_val += get_letter_value(letter)
        return total_val
    
    def is_in_both_compartments(self, item:str):
        if self.compartment_1.find(item) > -1 and self.compartment_2.find(item) > -1:
            return True
        return False