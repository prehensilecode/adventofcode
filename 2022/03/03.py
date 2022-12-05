#!/usr/bin/env python3
import sys, os

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
print(priorities)

with open('test.txt', 'r') as infile:
    common_items = []
    for line in infile:
        line_length = len(line.strip())
        print(line_length, line.strip(), line.strip()[:line_length//2], line.strip()[line_length//2:])
        left = set(line.strip()[:line_length//2])
        right = set(line.strip()[line_length//2:])
        intersection = left & right
        print(intersection)
        if intersection:
            for i in list(intersection):
                common_items.append(i)

print(common_items)
prio_sum = sum([priorities[i] for i in common_items])
print(prio_sum)

