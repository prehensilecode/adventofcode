#!/usr/bin/env python3
import sys
import os

debug_p = False


def is_visible(forest, y, x):
    global debug_p

    size = len(forest)

    retval = False

    # all trees on edges are visible
    if y == 0 or x == 0 or y == (size - 1) or x == (size - 1):
        retval = True
    else:
        tree = forest[y][x]
        row = forest[y]
        column = []
        for t in forest:
            column.append(t[x])

        if debug_p:
            print(f'DEBUG: forest[{y}][{x}] = {forest[y][x]}')
            print(f'DEBUG: row = {row}')
            print(f'DEBUG: column = {column}')

        if tree > max(row[:x]) or tree > max(row[x+1:]) or tree > max(column[:y]) or tree > max(column[y+1:]):
            retval = True

        if debug_p:
            print(f'DEBUG: retval = {retval}')

    return retval


forest = []
with open('input.txt', 'r') as infile:
    for l in infile:
        forest.append([int(i) for i in l.strip()])

for y in forest:
    print(y)
print(len(forest))

print(is_visible(forest, 0, 0))
print(is_visible(forest, 2, 3))
print(is_visible(forest, 2, 1))

size = len(forest)
n_visible = 0
for y in range(size):
    for x in range(size):
        if is_visible(forest, y, x):
            n_visible += 1

print(f'No. visible = {n_visible}')
