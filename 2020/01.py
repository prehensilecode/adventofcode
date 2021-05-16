#!/usr/bin/env python3
import sys
import os

n1 = []
with open('input', 'r') as f:
    for l in f:
        n1.append(int(l.strip()))

n2 = n1

count = 0
for count in range(len(n1)):
    for m in n2[count+1:]:
        if n1[count] + m == 2020:
            print(n1[count] * m)

