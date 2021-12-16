#!/usr/bin/env python3
import sys
import os

depths = []
with open('input1.txt', 'r') as f:
    for l in f:
        depths.append(int(l.strip()))

window_depths = []
for i in range(len(depths) - 2):
    window_depths.append(depths[i] + depths[i+1] + depths[i+2])

print(f'len(window_depths) = {len(window_depths)}')

n_incr = 0
for i in range(1, len(window_depths)):
    if window_depths[i] > window_depths[i-1]:
        n_incr += 1

print(n_incr)
