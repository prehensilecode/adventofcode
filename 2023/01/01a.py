#!/usr/bin/env python
import sys
import os

with open('input.txt', 'r') as f:
    sum = 0
    numstr = ""
    for l in f:
        for c in l:
            if c.isdigit():
                numstr += c

        sum += int(numstr[0] + numstr[-1])
        numstr = ""

print(sum)
