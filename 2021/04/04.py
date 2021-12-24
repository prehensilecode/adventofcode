#!/usr/bin/env python3
import sys

lines = []
with open('test.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

calls = [int(x) for x in lines[0].split(',')]
print(calls)
