#!/usr/bin/env python3
import sys, os

with open('test.txt', 'r') as infile:
    for line in infile:
        line_length = len(line.strip())
        print(line_length, line.strip(), line[:line_length//2], line[line_length//2:-1])
