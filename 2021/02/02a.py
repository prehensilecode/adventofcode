#!/usr/bin/env python3

class Position:
    def __init__(self):
        self.hor = 0
        self.depth = 0

    def move(self, course):
        with open(course, 'r') as f:
            for instruction in f:
                dir, amt = instruction.strip().split()
                amt = int(amt)

                if dir == 'forward':
                    self.hor += amt
                elif dir == 'down':
                    self.depth += amt
                elif dir == 'up':
                    self.depth -= amt

    def __repr__(self):
        return f'Hor. position = {self.hor}; Depth = {self.depth}'


pos = Position()
print(pos)
pos.move('input1.txt')
print(pos)
