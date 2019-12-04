#!/usr/bin/env python3
import sys
import os
import argparse

def read_inputs(filename):
    wires = []
    with open(filename, 'r') as f:
        for l in f:
            wires.append(l.strip().split(','))
    return wires


def parse_path(p):
    # p is something like "U23" = up 23 units
    # return (deltaX, deltaY)
    deltaX = 0
    deltaY = 0

    distance = int(p[1:])
    dir = p[0]

    if dir == 'U':
        deltaY = distance
    elif dir == 'D':
        deltaY = -distance
    elif dir == 'R':
        deltaX = distance
    elif dir == 'L':
        deltaX = -distance
    else:
        sys.exit(13)

    return (deltaX, deltaY)


def corners(wire):
    # return list of corners in given wire
    # start with coord (0,0)
    corners = [(0,0)]

    for p in wire:
        corners.append(parse_path(p))

    return corners

def main():
    parser = argparse.ArgumentParser("AoC 2.1")
    parser.add_argument('infile', metavar='infile', type=str, nargs=1, help='Input file')

    args = parser.parse_args()

    wires = read_inputs(args.infile[0])

    print(wires)

    wire_corners = [corners(w) for w in wires]

    print(wire_corners)

if __name__ == '__main__':
    main()
