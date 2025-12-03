#!/usr/bin/env python3

dial = 50
pw = 0

with open('input.txt', 'r') as f:
    for line in f:
        el = line.strip()
        [op, val] = [el[0], int(el[1:])]
        if op == 'L':
            dial = (dial - val) % 100
            if val >= dial:
                pw += 1 + (val % 100)
        elif op == 'R':
            dial = (dial + val) % 100
            if val >= (100 - dial):
                pw += 1 + (val % 100)

print(f'dial = {dial % 100}')
print(f'password = {pw}')

