#!/usr/bin/env python3
import sys
import os
import math

def fuel(mass):
    return int(math.floor(mass/3)) - 2

def main():
    masses = []
    with open("input.txt", "r") as f:
        for l in f:
            masses.append(int(l.strip()))

    sum = 0
    for m in masses:
        f = fuel(m)
        sum += f
        ff = fuel(f)
        while ff > 0:
            sum += ff
            ff = fuel(ff)

    print(sum)

if __name__ == '__main__':
    main()
