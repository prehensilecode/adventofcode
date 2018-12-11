#!/usr/bin/env python3
import sys
import os

# starting frequency 0
f0 = 0
print(f0)
with open('input.txt', 'r') as f:
    for l in f:
        f0 += int(l.strip())
        print(f0)

print("final freq = {}".format(f0))

