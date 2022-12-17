#!/usr/bin/env python3
import sys
import os

debug_p = False

# start of packet marker = 4 chars all different

def find_start(instr):
    global debug_p

    if debug_p:
        print(len(instr))
        print()

    markerlen = 4
    test = None
    for i in range(len(instr) - 2*markerlen):
        substr = instr[i:i+markerlen]
        test = set(substr)
        if len(test) < markerlen:
            continue
        else:
            if debug_p:
                print(f'Found: i = {i}, {instr[:i]}, res = {i+markerlen}')
            return i+markerlen


#example = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
#print(f'Start = {find_start(example)}')

with open('input.txt', 'r') as infile:
    for line in infile:
        print(f'Start = {find_start(line.strip())}')

