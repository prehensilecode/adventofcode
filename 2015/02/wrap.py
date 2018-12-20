#!/usr/bin/env python3.5
import sys
import os

def paper(dim):
    areas = [dim[0] * dim[1], dim[1] * dim[2], dim[2] * dim[0]]
    total = min(areas)
    for a in areas:
        total += 2 * a
    return total

def wrap(pkgs):
    tot = 0
    for p in pkgs:
        dim = [int(d) for d in p.strip().split('x')]
        tot += paper(dim)
    return tot

def ribbon(dim):
    dim.sort()
    tot = 2 * (dim[0] + dim[1])
    tot += dim[0] * dim[1] * dim[2]
    return tot

def tie(pkgs):
    tot = 0
    for p in pkgs:
        dim = [int(d) for d in p.strip().split('x')]
        tot += ribbon(dim)
    return tot



if __name__ == '__main__':
    pkgs = []
    with open('input.txt', 'r') as f:
        for l in f:
            pkgs.append(l)

    print('Total paper needed = {} ft^2'.format(wrap(pkgs)))
    print('Total ribbon needed = {} ft'.format(tie(pkgs)))


