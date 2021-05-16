#!/usr/bin/env python3
import sys
import os

def decode_pass(bp):
    # bp is a string of length 10
    # * first 7 chars = front/back (row)
    # * last 3 chars = left/right (col)
    # seat ID = row * 8 + col
    row_range = [0, 127]
    #print('row_range =', row_range)
    for r in bp[:7]:
        range_size = int((row_range[1] - row_range[0] + 1) / 2)
        if r == 'F':
            row_range = [row_range[0], row_range[0] + range_size - 1]
            #print(row_range)
        elif r == 'B':
            row_range = [row_range[0] + range_size, row_range[1]]
            #print(row_range)

    col_range = [0, 7]
    #print('col_range =', col_range)
    for c in bp[-3:]:
        range_size = int((col_range[1] - col_range[0] + 1) / 2)
        if c == 'L':
            col_range = [col_range[0], col_range[0] + range_size - 1]
            #print(col_range)
        elif c == 'R':
            col_range = [col_range[0] + range_size, col_range[1]]
            #print(col_range)

    #print('')
    #print('SEAT:', row_range, col_range)
    #print('- - - - - - - - - -')

    if (row_range[0] != row_range[1]) or (col_range[0] != col_range[1]):
        print('ERROR: row_range = {} ; col_range = {}'.format(row_range, col_range))
        sys.exit(1)
    
    return (8 * row_range[0] + col_range[0])


boarding_passes = []
with open('input05', 'r') as f:
    for l in f:
        boarding_passes.append(l.strip())

#print(boarding_passes)

seat_ids = []
for bp in boarding_passes:
    seat_ids.append(decode_pass(bp))

print('max. seat ID =', max(seat_ids))

