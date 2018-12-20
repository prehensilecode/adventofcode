#!/usr/bin/env python3.5
import sys
import os
import re

# instructions: turn on, turn off, toggle
# range: x,y through m,n
# e.g.
#  toggle 461,550 through 564,900
#  turn off 370,39 through 425,839
#  turn off 464,858 through 833,915
#  turn off 812,389 through 865,874
#  turn on 599,989 through 806,993
#  turn on 376,415 through 768,548
#  turn on 606,361 through 892,600

grid = []
for i in range(1000):
    grid.append([0 for j in range(1000)])

cmdpat = re.compile(r'^([a-z\ ]*)\s+(\d{1,3}\,\d{1,3})\s+through\s+(\d{1,3}\,\d{1,3})')

def zerogrid():
    global grid
    for i in range(1000):
        for j in range(1000):
            grid[i][j] = 0


def lights(directions):
    global grid
    global cmdpat

    zerogrid()

    for d in directions:
        m = cmdpat.match(d)
        if m:
            cmd = m.group(1)
            start = m.group(2)
            finish = m.group(3)

            i0, j0 = [int(n) for n in start.split(',')]
            i1, j1 = [int(n) for n in finish.split(',')]

            for i in range(i0, i1+1):
                for j in range(j0, j1+1):
                    if cmd == 'toggle':
                        if grid[i][j] == 1: grid[i][j] = 0
                        elif grid[i][j] == 0: grid[i][j] = 1
                    elif cmd == 'turn on':
                        grid[i][j] = 1
                    elif cmd == 'turn off':
                        grid[i][j] = 0


    tot = 0
    for r in grid:
        tot += sum(r)

    print(tot)


def dimmer(directions):
    global grid
    global cmdpat

    zerogrid()

    for d in directions:
        m = cmdpat.match(d)
        if m:
            cmd = m.group(1)
            start = m.group(2)
            finish = m.group(3)

            i0, j0 = [int(n) for n in start.split(',')]
            i1, j1 = [int(n) for n in finish.split(',')]

            for i in range(i0, i1+1):
                for j in range(j0, j1+1):
                    if cmd == 'toggle':
                        grid[i][j] += 2
                    elif cmd == 'turn on':
                        grid[i][j] += 1
                    elif cmd == 'turn off':
                        if grid[i][j] > 0: grid[i][j] -= 1


    tot = 0
    for r in grid:
        tot += sum(r)

    print(tot)



if __name__ == '__main__':
    directions = []
    with open('input.txt', 'r') as f:
        for l in f:
            directions.append(l)

    lights(directions)

    dimmer(directions)

