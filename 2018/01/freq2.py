#!/usr/bin/env python3
import sys
import os
import timeit

### NOTE have to keep applying the list of frequency changes ad infinitum

### from reddit Alfred456654
def foo():
    with open('input.txt', 'r') as of:
        nbs = list(map(int, list(map(str.strip, of.readlines()))))
        freqs_reached = set([0])
        freq = 0
        while True:
            for nb in nbs:
                freq += nb
                if freq in freqs_reached:
                    return freq
                freqs_reached.add(freq)

def bar():
    with open('input.txt', 'r') as f:
        dflist = list(map(int, list(map(str.strip, f.readlines()))))

    # starting frequency 0
    f0 = 0
    freqlist = [0]
    while True:
        for df in dflist:
            f0 += df
            if f0 in freqlist: 
                return f0
            else:
                freqlist.append(f0)
    

print("first dupe w/ foo = {}".format(foo()))

print("first dupe w/ bar = {}".format(bar()))

