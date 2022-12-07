#!/usr/bin/env python3
import sys, os

# groups of 3 lines

lower_prio = [n for n in range(1, 27)]
higher_prio = [n for n in range(27, 53)]
lower_alpha = [chr(n) for n in range(ord('a'), ord('z') + 1)]
higher_alpha = [chr(n) for n in range(ord('A'), ord('Z') + 1)]

#print(f'lower_prio = {lower_prio}')
#print(f'higher_prio = {higher_prio}')
#print(f'lower_alpha = {lower_alpha}')
#print(f'higher_alpha = {higher_alpha}')

lower = dict(zip(lower_alpha, lower_prio))
higher = dict(zip(higher_alpha, higher_prio))
priorities = lower | higher

#print(lower)
#print(higher)
#print(priorities)

with open('input.txt', 'r') as infile:
    elves = []
    for line in infile:
        elves.append(set(line.strip()))

badge = []
for i in range(0, 300, 3):
    intersection = elves[i + 0] & elves[i + 1] & elves[i + 2]
    if intersection:
        for j in list(intersection):
            badge.append(j)

prio_sum = sum(priorities[i] for i in badge)
print(prio_sum)
