#!/usr/bin/env python3
import sys
import os
import math


debug_p = True


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def metric(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)

    def touching(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return (dx <= 1) and (dy <= 1)

    def overlapping(self, other):
        return (self.metric(other) == 0)

    def __repr__(self):
        return f'({self.x}, {self.y})'


def step_r(h_pos, t_pos):
    if h_pos.metric(t_pos) > 1.5:
        print(f'ERROR: head-tail distance = {h_pos.metric(t_pos)}')
        sys.exit(5)

    new_h_pos = Position(h_pos.x, h_pos.y)
    new_t_pos = Position(t_pos.x, t_pos.y)

    if h_pos.metric(t_pos) <= 1:
        new_h_pos.x += 1

        if not new_t_pos.touching(new_h_pos):
            new_t_pos.x += 1
    else:
        new_h_pos.x += 1
        # diagonals: UR, LR, LL, UL
        if (h_pos.x > t_pos.x) and (h_pos.y > t_pos.y):
            new_t_pos.x += 1
            new_t_pos.y += 1
        elif (h_pos.x > t_pos.x) and (h_pos.y < t_pos.y):
            new_t_pos.x += 1
            new_t_pos.y -= 1
        elif (h_pos.x < t_pos.x) and (h_pos.y < t_pos.y):
            # still touching
            pass
        elif (h_pos.x < t_pos.x) and (h_pos.y > t_pos.y):
            # still touching
            pass

    return new_h_pos, new_t_pos


def move_r(h_pos, t_pos, dist):
    new_h_pos = h_pos
    new_t_pos = t_pos
    for _ in range(dist):
        new_h_pos, new_t_pos = step_r(new_h_pos, new_t_pos)

    return new_h_pos, new_t_pos


def step_l(h_pos, t_pos):
    if h_pos.metric(t_pos) > 1.4:
        print(f'ERROR: head-tail distance = {h_pos.metric(t_pos)}')
        sys.exit(7)

    new_h_pos = Position(h_pos.x, h_pos.y)
    new_t_pos = Position(t_pos.x, t_pos.y)

    if new_h_pos.metric(new_t_pos) <= 1:
        new_h_pos.x -= 1

        if not new_t_pos.touching(new_h_pos):
            new_t_pos.x -= 1
    else:
        new_h_pos.x -= 1
        # diagonals: UR, LR, LL, UL
        if (h_pos.x > t_pos.x) and (h_pos.y > t_pos.y):
            # still touching
            pass
        elif (h_pos.x > t_pos.x) and (h_pos.y < t_pos.y):
            # still touching
            pass
        elif (h_pos.x < t_pos.x) and (h_pos.y < t_pos.y):
            new_t_pos.x -= 1
            new_t_pos.y -= 1
        elif (h_pos.x < t_pos.x) and (h_pos.y > t_pos.y):
            new_t_pos.x -= 1
            new_t_pos.y += 1

    return new_h_pos, new_t_pos


def move_l(h_pos, t_pos, dist):
    new_h_pos = h_pos
    new_t_pos = t_pos
    for _ in range(dist):
        new_h_pos, new_t_pos = step_l(new_h_pos, new_t_pos)

    return new_h_pos, new_t_pos


def move_u(h_pos, t_pos, dist):
    pass


def move_d(h_pos, t_pos, dist):
    pass


def move_rope(h_pos, t_pos, move):
    # pos is a list [x, y]
    # move is a tuple (direc, dist)

    new_h_pos = h_pos
    new_t_pos = t_pos

    direc = move[0]
    dist = move[1]

    if direc == 'R':
        new_h_pos, new_t_pos = move_r(new_h_pos, new_t_pos, dist)
    elif direc == 'L':
        new_h_pos, new_t_pos = move_l(new_h_pos, new_t_pos, dist)
    elif direc == 'U':
        new_h_pos[1] += dist
    elif direc == 'D':
        new_h_pos[1] -= dist

    return new_h_pos, new_t_pos



# Snake - H & T start overlapping, say at (0, 0)

moves = []
with open('test.txt', 'r') as infile:
    for l in infile:
        tok = l.strip().split()
        direc = tok[0]
        dist = int(tok[1])
        moves.append((direc, dist))

for m in moves:
    print(m)
print()

if debug_p:
    h_pos = Position(0, 0)
    t_pos = Position(0, 0)
    print(f'DEBUG: h_pos = {h_pos}')
    print(f'DEBUG: t_pos = {t_pos}')
    print(f'DEBUG: h_pos.metric(t_pos) = {h_pos.metric(t_pos)}')
    print(f'DEBUG: h_pos.touching(t_pos) = {h_pos.touching(t_pos)}')
    print()

    h_pos = Position(0, 0)
    t_pos = Position(1, 1)
    print(f'DEBUG: h_pos = {h_pos}')
    print(f'DEBUG: t_pos = {t_pos}')
    print(f'DEBUG: h_pos.metric(t_pos) = {h_pos.metric(t_pos)}')
    print(f'DEBUG: h_pos.touching(t_pos) = {h_pos.touching(t_pos)}')
    print()

    h_pos = Position(1, 2)
    t_pos = Position(0, 0)
    print(f'DEBUG: h_pos = {h_pos}')
    print(f'DEBUG: t_pos = {t_pos}')
    print(f'DEBUG: h_pos.metric(t_pos) = {h_pos.metric(t_pos)}')
    print(f'DEBUG: h_pos.touching(t_pos) = {h_pos.touching(t_pos)}')
    print()

print("Move R")
h_pos = Position(1, 1)
t_pos = Position(0, 0)
print(f'Start: {h_pos}, {t_pos}')
h_pos, t_pos = move_rope(h_pos, t_pos, ('R', 4))
print(f'End: {h_pos}, {t_pos}')
print()

print("Move L")
h_pos = Position(0, 0)
t_pos = Position(0, 0)
print(f'Start: {h_pos}, {t_pos}')
h_pos, t_pos = move_rope(h_pos, t_pos, ('L', 4))
print(f'End: {h_pos}, {t_pos}')
print()
