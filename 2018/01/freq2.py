#!/usr/bin/env python3
import sys
import os

# starting frequency 0
f0 = 0
freqset = set()
freqset.add(f0)
with open('input.txt', 'r') as f:
    for l in f:
        f0 += int(l.strip())
        #print(f0)
        #print(freqset)
        #print("")

        #if f0 in freqset:
        #    print("found duplicate: {}".format(f0))
        #else:
        #    print("no duplicate: {}".format(f0))

        print(f0)

        freqset.add(f0)

print("final freq = {}".format(f0))
print("len(freqset) = {}".format(len(freqset)))

