#!/usr/bin/env python3
import sys
import os

depths = []
with open('input1.txt', 'r') as f:
    for l in f:
        depths.append(int(l.strip()))

n_incr = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        n_incr += 1

print(n_incr)
