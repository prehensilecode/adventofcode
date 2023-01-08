#!/usr/bin/env python3
import sys
import os

debug_p = False

# CPU
# - single register X
# - instructions
#   - addx V takes two cycles to complete. After two cycles, the X register is
#     increased by the value V. (V can be negative.)
#   - noop takes one cycle to complete. It has no other effect.

data = []
with open('input.txt', 'r') as infile:
    for line in infile:
        data.append(line.strip())

prog = []
for d in data:
    tok = d.split()
    if len(tok) == 1:
        # noop
        prog.append((tok[0],))
    elif len(tok) == 2:
        prog.append((tok[0], int(tok[1])))

if debug_p:
    for p in prog:
        print(p)

cycle = 1
x = 1
strength = 0
strength_chk = 0

for p in prog:
    if p[0] == 'noop':
        if (cycle == 20) or ((cycle - 20) % 40) == 0:
            strength = cycle * x
            strength_chk += strength

            if debug_p:
                print(f'cycle = {cycle}')
                print(f'x = {x}')
                print(f'strength = {strength}')
                print()
        cycle += 1
    elif p[0] == 'addx':
        if debug_p:
            print(f'FOO: cycle = {cycle}, x = {x}')

        if (cycle == 20) or ((cycle - 20) % 40) == 0:
            if debug_p:
                print(f'BAR: cycle = {cycle}, x = {x}')

            strength = cycle * x
            strength_chk += strength

            if debug_p:
                print(f'cycle = {cycle}')
                print(f'x = {x}')
                print(f'strength = {strength}')
                print()
        cycle += 1
        if (cycle == 20) or ((cycle - 20) % 40) == 0:
            if debug_p:
                print(f'BAZ: cycle = {cycle}, x = {x}')

            strength = cycle * x
            strength_chk += strength

            if debug_p:
                print(f'cycle = {cycle}')
                print(f'x = {x}')
                print(f'strength = {strength}')
                print()
        cycle += 1
        x += p[1]

print(f'strength_chk = {strength_chk}')

### Pt 2
### sprite is 3 px wide
### X reg sets hor. pos. of middle of sprite
### CRT is 40px wide x 6px high; zig zag top left to right
### px address is 0 based
### CRT paints px every cycle
