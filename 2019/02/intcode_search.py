#!/usr/bin/env python3
import sys
import os
import argparse

prog = None

def one(i1, i2, i3):
    global prog

    if prog[i1] >= len(prog) or prog[i2] >= len(prog) or prog[i3] >= len(prog):
        print("FOOBAR")
        return 1
    else:
        prog[prog[i3]] = prog[prog[i1]] + prog[prog[i2]]
        return 0

def two(i1, i2, i3):
    global prog

    if prog[i1] >= len(prog) or prog[i2] >= len(prog) or prog[i3] >= len(prog):
        print("BARFOO")
        return 1
    else:
        prog[prog[i3]] = prog[prog[i1]] * prog[prog[i2]]
        return 0

def compute():
    global prog

    for c in range(0, len(prog), 4):
        if prog[c] == 1:
            if one(c+1, c+2, c+3) == 0:
                continue
            else:   
                return 1
        elif prog[c] == 2:
            if two(c+1, c+2, c+3) == 0:
                continue
            else:   
                return 1
        elif prog[c] == 99:
            break

    #print("result = {}".format(prog))
    return 0

def main():
    global prog
    
    parser = argparse.ArgumentParser("AoC 2.1")
    parser.add_argument('infile', metavar='infile', type=str, nargs=1, help='Input file')

    args = parser.parse_args()

    print("Reading intcode program from: {}".format(args.infile[0]))

    with open(args.infile[0], 'r') as f:
        prog = [ int(i) for i in f.read().strip().split(',')]

    print("prog = {}".format(prog))


    for verb in range(100):
        for noun in range(100):
            # reset prog
            with open(args.infile[0], 'r') as f:
                prog = [ int(i) for i in f.read().strip().split(',')]

            prog[1] = noun
            prog[2] = verb
            if compute() == 0:
                if prog[0] == 19690720:
                    print("noun = {} ; verb = {} ; result = {}".format(noun, verb, prog[0]))
            else:
                print("BAH: result = {}".format(prog[0]))
                continue

if __name__ == '__main__':
    main()

