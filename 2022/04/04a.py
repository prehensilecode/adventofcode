#!/usr/bin/env python3

with open('input.txt', 'r') as inputfile:
    assignments = []
    for line in inputfile:
        assignments.append([i.split('-') for i in line.strip().split(',')])

overlap = 0
for a in assignments:
    if (int(a[0][0]) <= int(a[1][0])) and (int(a[0][1]) >= int(a[1][1])):
        overlap += 1
    elif (int(a[1][0]) <= int(a[0][0])) and (int(a[1][1]) >= int(a[0][1])):
        overlap += 1
    elif (int(a[0][0]) <= int(a[1][0])) and (int(a[0][1]) >= int(a[1][0])):
        overlap += 1
    elif (int(a[1][0]) <= int(a[0][0])) and (int(a[1][1]) >= int(a[0][0])):
        overlap += 1

print(overlap)
