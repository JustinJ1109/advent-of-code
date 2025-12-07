from typing import List


class Dial:
    
    def __init__(self, start_pos: int = 50, min: int = 0, max: int = 99):
        self.cur = start_pos
        self.min = min
        self.max = max

        self.dirmap = {
            "L": self.rot_left,
            "R": self.rot_right
        }

    def rot_left(self, n: int):
        self.cur -= n 
        
        ct = 0
        while self.cur < self.min:
            self.cur += (self.max + 1)
            ct += 1
        return ct
        
    def rot_right(self, n: int):
        self.cur += n
        
        ct = 0
        while self.cur > self.max:
            self.cur -= (self.max + 1)
            ct += 1
        return ct

def solve_1(solution_input: List[str], *args, **kwargs):
    dial = Dial()

    spin = lambda direction, n: dial.dirmap[direction](n)
    count = 0
    for l in solution_input:
        direction, n = l[0], int(l[1:])

        spin(direction, n)
        if dial.cur == 0:
            count += 1
    return count

def solve_2(solution_input: List[str]):
    dial = Dial()
    spin = lambda direction, n: dial.dirmap[direction](n)
    count = 0
    for l in solution_input:
        direction, n = l[0], int(l[1:])

        count += spin(direction, n)
        # if dial.cur == 0:
            # count += 1
    return count