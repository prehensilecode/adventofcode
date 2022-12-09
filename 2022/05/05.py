#!/usr/bin/env python3
import sys
import os
 

def read_stack_line(n_stacks, stack_line_str):
    # a line looks like "  [A]   [B]" ...
    # using 0-base index
    # 1st col letters are in the 1st position
    # 2nd col letters are in the 5th position
    # 3rd col letters are in the 9th position
    # len() indicates how many cols
    print(stack_line_str)
    n_stacks = (len(stack_line_str) - 3) // 4 + 1
    print(f'n_stacks = {n_stacks}')


lines = []
with open('input.txt', 'r') as infile:
    for line in infile:
        lines.append(line.rstrip())

count = 0
line = lines[count]
while line:
    count += 1
    line = lines[count]

n_stacks = int(lines[count - 1][-1])
print(f'n_stacks = {n_stacks}')

for i in range(n_stacks):
    read_stack_line(n_stacks, lines[i])
