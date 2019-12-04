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
    corners = [[0,0]]

    for p in wire:
        delta = parse_path(p)
        c = [ corners[-1][i] + delta[i] for i in range(2) ]
        corners.append(c)

    return corners


def intersections(wire_corners):
    print(wire_corners[0])
    print(wire_corners[1])

    x = []

    # this is an N^2 search?
    for i in range(len(wire_corners[0]) - 1):
        for j in range(len(wire_corners[1]) - 1):
            # wire[0] horizontal, wire[1] vertical
            if (wire_corners[0][i][1] == wire_corners[0][i+1][1]) and (wire_corners[1][j][0] == wire_corners[1][j+1][0]):
                if ( (wire_corners[0][i+1][1] > wire_corners[1][j][1]) and (wire_corners[0][i+1][1] < wire_corners[1][j+1][1]) ) or ( (wire_corners[0][i+1][1] > wire_corners[1][j+1][1]) and (wire_corners[0][i+1][1] < wire_corners[1][j][1]) ):
                    if ((wire_corners[0][i][0] < wire_corners[1][j+1][0]) and (wire_corners[0][i+1][0] > wire_corners[1][j+1][0])) or ((wire_corners[0][i+1][0] < wire_corners[1][j+1][0]) and (wire_corners[0][i][0] > wire_corners[1][j+1][0])):
                        x.append([wire_corners[1][j][0], wire_corners[0][i][1]])
            # wire[0] vertical, wire[1] horizontal
            elif (wire_corners[0][i][0] == wire_corners[0][i+1][0]) and (wire_corners[1][j][1] == wire_corners[1][j+1][1]):
                if ( (wire_corners[1][j+1][1] > wire_corners[0][i][1]) and (wire_corners[1][j+1][1] < wire_corners[0][i+1][1]) ) or ( (wire_corners[1][j+1][1] > wire_corners[0][i+1][1]) and (wire_corners[1][j+1][1] < wire_corners[0][i][1]) ):
                    if ( (wire_corners[1][j][0] < wire_corners[0][i+1][0]) and (wire_corners[1][j+1][0] > wire_corners[0][i+1][0]) ) or ( (wire_corners[1][j+1][0] < wire_corners[0][i+1][0]) and (wire_corners[1][j][0] > wire_corners[0][i+1][0]) ):
                        x.append([wire_corners[0][i][0], wire_corners[1][j][1]])
            else:
                continue

    return x



def main():
    parser = argparse.ArgumentParser("AoC 2.1")
    parser.add_argument('infile', metavar='infile', type=str, nargs=1, help='Input file')

    args = parser.parse_args()

    wires = read_inputs(args.infile[0])

    print(wires)

    wire_corners = [corners(w) for w in wires]

    x = intersections(wire_corners)

    print("x = {}".format(x))

    dists = [ sum(y) for y in [ map(abs, junc) for junc in x ] ]

    print("min. dist. = {}".format(min(dists)))

if __name__ == '__main__':
    main()

