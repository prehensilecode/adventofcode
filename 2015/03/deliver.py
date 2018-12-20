#!/usr/bin/env python3.5
import sys
import os

def deliver(directions):
    this = (0,0)
    houses = {this: 1}
    for d in directions:
        if d == '^':
            this = (this[0], this[1]+1)
        elif d == 'v':
            this = (this[0], this[1]-1)
        elif d == '<':
            this = (this[0]-1, this[1])
        elif d == '>':
            this = (this[0]+1, this[1])

        if this in houses:
            houses[this] += 1
        else:
            houses[this] = 1

    print(len(houses))

def robodeliver(directions):
    this_santa = (0,0)
    this_robo  = (0,0)
    houses = {this_santa: 1}
    for i in range(0, len(directions), 2):
        d_santa = directions[i]
        d_robo  = directions[i+1]
        if d_santa == '^':
            this_santa = (this_santa[0], this_santa[1]+1)
        elif d_santa == 'v':
            this_santa = (this_santa[0], this_santa[1]-1)
        elif d_santa == '<':
            this_santa = (this_santa[0]-1, this_santa[1])
        elif d_santa == '>':
            this_santa = (this_santa[0]+1, this_santa[1])

        if this_santa in houses:
            houses[this_santa] += 1
        else:
            houses[this_santa] = 1

        if d_robo == '^':
            this_robo = (this_robo[0], this_robo[1]+1)
        elif d_robo == 'v':
            this_robo = (this_robo[0], this_robo[1]-1)
        elif d_robo == '<':
            this_robo = (this_robo[0]-1, this_robo[1])
        elif d_robo == '>':
            this_robo = (this_robo[0]+1, this_robo[1])

        if this_robo in houses:
            houses[this_robo] += 1
        else:
            houses[this_robo] = 1

    print(len(houses))

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        directions = f.read()
    deliver(directions)
    robodeliver(directions)
    

