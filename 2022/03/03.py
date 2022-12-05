#!/usr/bin/env python3
import sys, os

lower_prio = [n for n in range(1, 27)]
higher_prio = [n for n in range(27, 53)]
lower_alpha = [chr(n) for n in range(ord('a'), ord('z') + 1)]
higher_alpha = [chr(n) for n in range(ord('A'), ord('Z') + 1)]

print(f'lower_prio = {lower_prio}')
print(f'higher_prio = {higher_prio}')
print(f'lower_alpha = {lower_alpha}')
print(f'higher_alpha = {higher_alpha}')

with open('test.txt', 'r') as infile:
    for line in infile:
        line_length = len(line.strip())
        print(line_length, line.strip(), line[:line_length//2], line[line_length//2:-1])
