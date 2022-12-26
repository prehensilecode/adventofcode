#!/usr/bin/env python3
import sys
import os
from operator import mul, itemgetter

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
        col = []
        for t in forest:
            col.append(t[x])

        if debug_p:
            print(f'DEBUG: forest[{y}][{x}] = {forest[y][x]}')
            print(f'DEBUG: row = {row}')
            print(f'DEBUG: col = {col}')

        if tree > max(row[:x]) or tree > max(row[x+1:]) or tree > max(col[:y]) or tree > max(col[y+1:]):
            retval = True

        if debug_p:
            print(f'DEBUG: retval = {retval}')

    return retval


def scenic_score(forest, y, x):
    global debug_p

    if debug_p:
        print(f'DEBUG: scenic_score(): y = {y}, x = {x}')

    size = len(forest)

    retval = 0

    if y == 0 or x == 0 or y == (size - 1) or x == (size - 1):
        pass
    else:
        tree = forest[y][x]
        row = forest[y]
        col = []
        for t in forest:
            col.append(t[x])

        score = []

        # look left
        vs = 0
        for i in range(x-1, -1, -1):
            if row[i] <= tree:
                vs += 1
                if row[i] == tree:
                    break

        score.append(vs)

        # look right
        vs = 0
        for i in range(x+1, size):
            if row[i] <= tree:
                vs += 1
                if row[i] == tree:
                    break

        score.append(vs)

        # look up
        vs = 0
        for i in range(y-1, -1, -1):
            if col[i] <= tree:
                vs += 1
                if col[i] == tree:
                    break

        score.append(vs)

        # look down
        vs = 0
        for i in range(y+1, size):
            if col[i] <= tree:
                vs += 1
                if col[i] == tree:
                    break

        score.append(vs)

        retval = 1
        for s in score:
            retval *= s

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

### Part 2


if debug_p:
    y = 1
    x = 2 
    print(f'DEBUG: scenic_score(forest, {y}, {x}) = {scenic_score(forest, y, x)}')
    print(f'DEBUG: expect scenic_score(forest, {y}, {x}) = 4')
    print(f'DEBUG: expect scenic_score(forest, {y}, {x}) list = [1, 2, 1, 2]')

scores = {}
for y in range(size):
    for x in range(size):
        scores[(y, x)] = scenic_score(forest, y, x)

#for k,v in scores.items():
#    if v > 0:
#        print(k, v)

# see https://stackoverflow.com/a/268285

print(scores[max(scores, key=scores.get)])

print(scores[max(scores.items(), key=itemgetter(1))[0]])

