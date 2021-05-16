#!/usr/bin/env python3
import sys
import os

def vecsum(a, b):
    global width
    global height

    return [(a[0] + b[0]) % width, a[1] + b[1]]

map = []
with open('input03', 'r') as f:
    for l in f:
        map.append(l.strip())


width = len(map[0])
height = len(map)
print('width = {}, height = {}'.format(width, height))

directions = [3, 1]
pos = [0, 0]
num_trees = 0
for rowcount in range(height-1):
    new_pos = vecsum(pos, directions)
    if map[new_pos[1]][new_pos[0]] == '#':
        num_trees += 1

    pos = new_pos.copy()

print('Num. trees = {}'.format(num_trees))

print('- - - - - - - - - -')

dirs = ([1, 1], [3, 1], [5, 1], [7, 1], [1, 2])
pos = [0, 0]
num_trees = 0
product = 1
for dir in dirs:
    print(dir)
    for rowcount in range(height-1):
        new_pos = vecsum(pos, dir)
        if new_pos[1] < height and map[new_pos[1]][new_pos[0]] == '#':
            num_trees += 1

        pos = new_pos.copy()
    print('Num. trees = {}'.format(num_trees))
    product *= num_trees
    num_trees = 0
    pos = [0, 0]

print('Prod. of num. trees = {}'.format(product))
    
