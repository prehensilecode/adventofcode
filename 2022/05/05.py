#!/usr/bin/env python3
import sys
import os
import re
 
debug_p = False

def read_stack_line_re(n_stacks, stack_line_str):
    global debug_p

    row = ['-' for n in range(n_stacks)]
    if debug_p:
        print(f'DEBUG: read_stack_line_re: row = {row}')

    # c.start() ==  0 -> 1st col
    # c.start() ==  4 -> 2nd col
    # c.start() ==  8 -> 3rd col
    # c.start() == 12 -> 4th col
    # ...
    crate_pat = re.compile(r'\[(\w)\]')
    for c in re.finditer(crate_pat, stack_line_str):
        if debug_p:
            print('%02d-%02d: %s; %s' % (c.start(), c.end(), c.group(0), c.group(1)))
        row[c.start() // 4] = c.group(1)

    return row


def read_stack_line(n_stacks, stack_line_str):
    global debug_p

    # a line looks like "  [A]   [B]" ...
    # using 0-base index
    # 1st col letters are in the 1st position
    # 2nd col letters are in the 5th position
    # 3rd col letters are in the 9th position
    # len() indicates how many cols
    if debug_p:
        print(stack_line_str)

    n_stacks = (len(stack_line_str) - 3) // 4 + 1

    if debug_p:
        print(f'n_stacks = {n_stacks}')


def main():
    global debug_p

    lines = []
    with open('input.txt', 'r') as infile:
        for line in infile:
            lines.append(line.rstrip())

    count = 0
    while lines[count]:
        count += 1

    n_stacks = int(lines[count - 1][-1])
    height = count - 1

    if debug_p:
        print(f'n_stacks = {n_stacks}')
        print(f'max. height = {height}')

    for i in range(n_stacks):
        row = read_stack_line_re(n_stacks, lines[i])
        print(row)


if __name__ == '__main__':
    main()
