f = open("9/input.txt", "r")
input_text = f.read()



class Rope():
    def __init__(self, num_of_knots) -> None:
        self.head_knot = Knot(0, None)
        self.knots = []
        knot_to_follow = self.head_knot
        for num in range(1, num_of_knots+1):
            new_knot = Knot(num, knot_to_follow)
            self.knots.append(new_knot)
            knot_to_follow = new_knot
    
    def move(self, direction, amt):
        for i in range(0, amt):
            if direction =="R":
                self.move_head(-1, 'x')
                self.move_tail_knots()
            if direction =="L":
                self.move_head(1, 'x')
                self.move_tail_knots()
            if direction =="U":
                self.move_head(-1, 'y')
                self.move_tail_knots()
            if direction =="D":
                self.move_head(1, 'y')
                self.move_tail_knots()

    def move_tail_knots(self):
        for knot in self.knots:
            knot.move_tail()

    def move_head(self, dir, plane):
        if plane == 'x':
            self.head_knot.x += dir
        if plane == 'y':
            self.head_knot.y += dir
        

class Knot():
    def __init__(self, num, knot_to_follow):
        if knot_to_follow:
            self.leader_knot = knot_to_follow
        self.x = 0
        self.y = 0
        self.knot_positions = [(0,0)]
        self.knot_num = num
    
    
    def move_tail(self):
        if self.check_if_tail_is_touching_head():
            return
        if self.leader_knot.x == self.x:
            if (self.leader_knot.y-self.y) < 0:
                self.move_tail_step(-1, 'y')
                self.record_tail_pos()
                return
            else:
                self.move_tail_step(1, 'y')
                self.record_tail_pos()
                return
        if self.leader_knot.y == self.y:
            if (self.leader_knot.x-self.x) < 0:
                self.move_tail_step(-1, 'x')
                self.record_tail_pos()
                return
            else:
                self.move_tail_step(1, 'x')
                self.record_tail_pos()
                return
        if (self.leader_knot.x-self.x) < 0:
            self.move_tail_step(-1, 'x')
        else:
            self.move_tail_step(1, 'x')

        if (self.leader_knot.y-self.y) < 0:
            self.move_tail_step(-1, 'y')
        else:
            self.move_tail_step(1, 'y')
        
        self.record_tail_pos()
        
        return

    def record_tail_pos(self):
        self.knot_positions.append((self.x, self.y))

    def move_tail_step(self, dir, plane):
        if plane == 'x':
            self.x += dir
        if plane == 'y':
            self.y += dir

    def check_if_tail_is_touching_head(self):
        if self.leader_knot.x == self.x and self.leader_knot.y == self.y:
            return True
        if self.leader_knot.x == self.x and (self.y ==self.leader_knot.y+1 or self.y ==self.leader_knot.y-1):
            return True
        if self.leader_knot.y == self.y and (self.x ==self.leader_knot.x+1 or self.x ==self.leader_knot.x-1):
            return True
        if (self.x == self.leader_knot.x+1 and self.y ==self.leader_knot.y-1) or (self.x == self.leader_knot.x-1 and self.y ==self.leader_knot.y-1) or(self.x == self.leader_knot.x+1 and self.y ==self.leader_knot.y+1) or (self.x == self.leader_knot.x-1 and self.y ==self.leader_knot.y+1): 
            return True
        return False




instructions = []
for line in input_text.splitlines():
    instructions.append((line.split()))
# print(instructions)

rope = Rope(9)
for dir, amt in instructions:
    rope.move(dir, int(amt))

print(rope.knots)
for knot in rope.knots:
    print()
    unque_pos = set(knot.knot_positions)
    print(f"Knot num {knot.knot_num} has {len(unque_pos)} unique positions")