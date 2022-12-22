f = open("13/input.txt", "r")
input_text = f.read()
from typing import List
import ast
class Signal():
    def __init__(self, signal1, index) -> None:
        self.signal= self.process_signal(signal1)
        self.original_signal_str = signal1
        self.index = index
                  
    def process_signal(self, signal):
        return ast.literal_eval(signal)

    def check_valid(self, signal_2):
        self.valid = self.compare_signals(self.signal_1, signal_2.signal)

    def compare_signals(self, signal_1, signal_2):
        validity = None
        try:
            for idx, el in enumerate(signal_1):
                comparator_type = self.check_type(el, signal_2[idx])
                if comparator_type == "int":
                    validity = self.compare_nums(el, signal_2[idx])
                if comparator_type == "mixed_types":
                    validity = self.mixed_types(el, signal_2[idx])
                if comparator_type == "lists":
                    validity = self.compare_signals(el, signal_2[idx])
                if validity != None:
                    break
        except IndexError:
            pass
        if validity == None:
            if len(signal_1) < len(signal_2):
                return True
            if len(signal_1) > len(signal_2):
                return False
        return validity

    def mixed_types(self, num1, num2):
        if type(num1) == int:
            return self.compare_signals([num1], num2)
        if type(num2) == int:
            return self.compare_signals(num1, [num2])

    def compare_nums(self, num1, num2):
        if num1 < num2:
            return True
        if num1 > num2:
            return False
        return None

    def check_type(self, val, val2):
        if type(val) == int and type(val2) == int:
            return "int"
        if type(val) == int or type(val2) == int:
            return "mixed_types"
        if type(val) == list or type(val2) == list:
            return "lists"

    def __lt__(self, other):     
        return self.compare_signals(self.signal, other.signal)

        
        
lines = input_text.splitlines()
count_of_pairs = int((len(lines)+1) / 3)
print(count_of_pairs)
all_signals = []
num = 1
for i in range(0, count_of_pairs):
    signal_lines = lines[i*3:3+i*3]
    new_signal = Signal(signal_lines[0], num)
    num += 1
    new_signal_2 = Signal(signal_lines[1], num)
    num += 1
    all_signals.append(new_signal)
    all_signals.append(new_signal_2)

all_signals.append(Signal("[[2]]", num))
num += 1
all_signals.append(Signal("[[6]]", num))
sig_sum = 1

all_signals = sorted(all_signals)
for idx, signal in enumerate(all_signals):
    # print(signal.signal)
    if signal.original_signal_str == "[[2]]" or signal.original_signal_str == "[[6]]" :
        sig_sum = sig_sum*(idx+1)

print("Decode product is", sig_sum)

