#!/usr/bin/env python3

with open('input.txt', 'r') as inputfile:
    assignments = []
    for line in inputfile:
        assignments.append([i.split('-') for i in line.strip().split(',')])

assgn = []
for a in assignments:
    assgn.append([[int(i) for i in a[0]], [int(j) for j in a[1]]])

contain = 0
for a in assgn:
    #print(a[0][0], a[0][1], a[1][0], a[1][1])
    if (a[0][0] <= a[1][0]) and (a[0][1] >= a[1][1]):
        #print('foo', a[0][0], '<=', a[1][0], 'and', a[0][1], '>=', a[1][1])
        contain += 1
    elif (a[1][0] <= a[0][0]) and (a[1][1] >= a[0][1]):
        #print('bar', a)
        contain += 1

print(contain)
