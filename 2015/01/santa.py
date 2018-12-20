#!/usr/bin/env python3.5
import sys
import os


def santa(instr):
    pos = 0
    i = 0
    for c in instr:
        i += 1
        if c == '(':
            pos += 1
        elif c == ')':
            pos -= 1

        if pos == -1:
            print('Entered basement on instruction #{}'.format(i))

    print(pos)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        instr = f.read()
    santa(instr)

