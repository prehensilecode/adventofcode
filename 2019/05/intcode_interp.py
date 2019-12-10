#!/usr/bin/env python3
import sys
import os
import argparse

prog = None

def one(i1, i2, i3):
    global prog

    prog[prog[i3]] = prog[prog[i1]] + prog[prog[i2]]

def two(i1, i2, i3):
    global prog

    prog[prog[i3]] = prog[prog[i1]] * prog[prog[i2]]


def main():
    global prog
    
    parser = argparse.ArgumentParser("AoC 2.1")
    parser.add_argument('infile', metavar='infile', type=str, nargs=1, help='Input file')

    args = parser.parse_args()

    print("Reading intcode program from: {}".format(args.infile[0]))

    with open(args.infile[0], 'r') as f:
        prog = [ int(i) for i in f.read().strip().split(',')]

    print("prog = {}".format(prog))

    for c in range(0, len(prog), 4):
        if prog[c] == 1:
            one(c+1, c+2, c+3)
            continue
        elif prog[c] == 2:
            two(c+1, c+2, c+3)
            continue
        elif prog[c] == 99:
            break

    print("result = {}".format(prog))

if __name__ == '__main__':
    main()

