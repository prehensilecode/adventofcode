#!/usr/bin/env python3

with open('input.txt', 'r') as inputfile:
    assignments = []
    for line in inputfile:
        assignments.append([i.split('-') for i in line.strip().split(',')])

#print(f'no. of assignments: {len(assignments)}')
#print(f'last assignment: {assignments[-1]}')

contain = 0
for a in assignments:
    #print(a[0][0], a[0][1], a[1][0], a[1][1])
    if (int(a[0][0]) <= int(a[1][0])) and (int(a[0][1]) >= int(a[1][1])):
        #print('foo', a[0][0], '<=', a[1][0], 'and', a[0][1], '>=', a[1][1])
        contain += 1
    elif (int(a[1][0]) <= int(a[0][0])) and (int(a[1][1]) >= int(a[0][1])):
        #print('bar', a)
        contain += 1

print(contain)
