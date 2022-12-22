f = open("9/input.txt", "r")
input_text = f.read()


class RopeMove():
    def __init__(self):
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0
        self.tail_positions = [(0,0)]
    
    def move(self, direction, amt):
        for i in range(0, amt):
            if direction =="R":
                self.move_head(-1, 'x')
                self.move_tail()
            if direction =="L":
                self.move_head(1, 'x')
                self.move_tail()
            if direction =="U":
                self.move_head(-1, 'y')
                self.move_tail()
            if direction =="D":
                self.move_head(1, 'y')
                self.move_tail()

    def move_head(self, dir, plane):
        if plane == 'x':
            self.head_x += dir
        if plane == 'y':
            self.head_y += dir
    
    
    def move_tail(self):
        if self.check_if_tail_is_touching_head():
            return
        if self.head_x == self.tail_x:
            if (self.head_y-self.tail_y) < 0:
                self.move_tail_step(-1, 'y')
                self.record_tail_pos()
                return
            else:
                self.move_tail_step(1, 'y')
                self.record_tail_pos()
                return
        if self.head_y == self.tail_y:
            if (self.head_x-self.tail_x) < 0:
                self.move_tail_step(-1, 'x')
                self.record_tail_pos()
                return
            else:
                self.move_tail_step(1, 'x')
                self.record_tail_pos()
                return
        if (self.head_x-self.tail_x) < 0:
            self.move_tail_step(-1, 'x')
        else:
            self.move_tail_step(1, 'x')

        if (self.head_y-self.tail_y) < 0:
            self.move_tail_step(-1, 'y')
        else:
            self.move_tail_step(1, 'y')
        
        
        self.record_tail_pos()
        
        return

    def record_tail_pos(self):
        self.tail_positions.append((self.tail_x, self.tail_y))



    def move_tail_step(self, dir, plane):
        if plane == 'x':
            self.tail_x += dir
        if plane == 'y':
            self.tail_y += dir

    def check_if_tail_is_touching_head(self):
        if self.head_x == self.tail_x and self.head_y == self.tail_y:
            return True
        if self.head_x == self.tail_x and (self.tail_y ==self.head_y+1 or self.tail_y ==self.head_y-1):
            return True
        if self.head_y == self.tail_y and (self.tail_x ==self.head_x+1 or self.tail_x ==self.head_x-1):
            return True
        if (self.tail_x == self.head_x+1 and self.tail_y ==self.head_y-1) or (self.tail_x == self.head_x-1 and self.tail_y ==self.head_y-1) or(self.tail_x == self.head_x+1 and self.tail_y ==self.head_y+1) or (self.tail_x == self.head_x-1 and self.tail_y ==self.head_y+1): 
            return True
        return False




instructions = []
for line in input_text.splitlines():
    instructions.append((line.split()))
# print(instructions)

rope = RopeMove()
for dir, amt in instructions:
    rope.move(dir, int(amt))


unque_pos = set(rope.tail_positions)
print(len(unque_pos))