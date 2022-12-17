#!/usr/bin/env python3
import sys
import os
import re
import numpy as np
import argparse
 
debug_p = False


def make_moves(crates_by_col, moves, version=9000):
    global debug_p

    if debug_p:
        print(crates_by_col)
        print(moves)

    if debug_p:
        print('Making moves:')

    for m in moves:
        height = len(crates_by_col[m[1]])
        start = height - m[0]

        if version == 9000:
            crates_by_col[m[2]] += reversed(crates_by_col[m[1]][start:])
        elif version == 9001:
            crates_by_col[m[2]] += crates_by_col[m[1]][start:]
        else:
            print(f'Unknown CrateMover version {version}')
            sys.exit(69)

        del crates_by_col[m[1]][start:]

        if debug_p:
            for c in crates_by_col:
                print(c)
            print()

    if debug_p:
        print('Done moving.')


def parse_instruction(instr):
    # move qty from col no. to other col no.
    tok = instr.split()
    qty = int(tok[1])
    src = int(tok[3]) - 1
    dst = int(tok[5]) - 1

    return (qty, src, dst)


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

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', metavar='version', type=int, default=9000, help='CrateMover version')
    args = parser.parse_args()

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

    crates = []
    for i in range(height):
        row = read_stack_line_re(n_stacks, lines[i])
        crates.insert(0, row)

    if debug_p:
        for row in crates:
            print(row)
        print()

    crates_by_col = np.array(crates).T.tolist()

    for col in crates_by_col:
        for i in reversed(range(len(col))):
            if col[i] == '-':
                del col[i]

    if debug_p:
        for col in crates_by_col:
            print(col)
        print()

        print(f'lines[count] = {lines[count]}')
        print(f'lines[count+1] = {lines[count+1]}')

    moves = []
    instructions = lines[count+1:]
    for instr in instructions:
        moves.append(parse_instruction(instr))

    make_moves(crates_by_col, moves, version=args.version)
    result = []
    for c in crates_by_col:
        if debug_p:
            print(c)
        result.append(c[-1])

    print(''.join(result))


if __name__ == '__main__':
    main()
