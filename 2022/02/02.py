#!/usr/bin/env python3
import sys, os
from enum import IntEnum, unique

# A, X = Rock = 1; B, Y = Paper = 2; C, Z = Scissors = 3
# A > Z; B > X; C > Y

# score = shape + wld (wld = 0 for loss, 3 for draw, 6 for win)

scoring_table = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
                 ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
                 ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}

shape_value = {'X': 1, 'Y': 2, 'Z': 3}


def score(opp, me):
    return scoring_table[(opp, me)] + shape_value[me]


#print(f'(A, X) - expect 4; get {score("A", "X")}')
#print(f'(A, Y) - expect 8; get {score("A", "Y")}')

my_score = 0
with open('strat.txt', 'r') as stratfile:
    for line in stratfile:
        opp, me = line.strip().split()
        my_score += score(opp, me)

print(f'Total score: {my_score}')

