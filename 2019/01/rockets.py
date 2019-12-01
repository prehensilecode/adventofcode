#!/usr/bin/env python3
import sys
import os
import math

def main():
    masses = []
    with open("input.txt", "r") as f:
        for l in f:
            masses.append(int(l.strip()))

    sum = 0
    for m in masses:
        sum += int(math.floor(m/3)) - 2

    print(sum)

if __name__ == '__main__':
    main()
