#!/usr/bin/env python3
import sys
import os

debug_p = False

# start of packet marker = 4 chars all different
# start of message marker = 14 chars all different

def find_start(instr, markerlen):
    global debug_p

    if debug_p:
        print(len(instr))
        print()

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
        print(f'Start = {find_start(line.strip(), 4)}')

with open('input.txt', 'r') as infile:
    for line in infile:
        print(f'Start = {find_start(line.strip(), 14)}')
