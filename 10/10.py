f = open("10/input.txt", "r")
input_text = f.read()

value_v = 1
cycle_num = 0
values_of_v = []

class Cpu():
    def __init__(self) -> None:
        self.cycle = 0
        self.v  = 1
        self.record_v_per_cycle = [1]
        self.crt = []
        self.crt_pos = 0

    def noop(self):
        self.record_v_per_cycle.append(self.v)
        self.draw_crt()
        self.cycle += 1

    def addx(self, num):
        self.record_v_per_cycle.append(self.v)
        self.draw_crt()
        self.cycle += 1
        self.record_v_per_cycle.append(self.v)
        self.draw_crt()
        self.cycle += 1
        self.v += num
    

    def increment_crts_pos(self):
        if self.crt_pos < 40:
            self.crt_pos +=1
        if self.crt_pos > 39:
            self.crt_pos = 0

    def draw_crt(self):
        sprite_pos = [self.v-1, self.v, self.v+1]
        # print(self.crt_pos, sprite_pos)
        if self.crt_pos in sprite_pos:
            self.crt.append("#")
        else:
            self.crt.append(".")
        self.increment_crts_pos()


    def get_signal_strength(self, cycle_num):
        return cycle_num * self.record_v_per_cycle[cycle_num]

test_cpu = Cpu()

for line in input_text.splitlines():
    if line.strip() == "noop":
        test_cpu.noop()
    else:
        command, value = line.split()
        test_cpu.addx(int(value))


sum_signals = [20,60, 100, 140, 180, 220]
total_sum = 0
# print(test_cpu.record_v_per_cycle)
for cycle in sum_signals:
    print("signal strenght at %i: %i" % (cycle, test_cpu.get_signal_strength(cycle)))
    total_sum += test_cpu.get_signal_strength(cycle)
print("Total sum:", total_sum)

i = 0
while i < len(test_cpu.crt):
    string_row = ""
    for r in range(40):
        string_row += str(test_cpu.crt[i])
        i += 1
    print(string_row)