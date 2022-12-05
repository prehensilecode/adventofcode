#!/usr/bin/env python3
import sys, os
from enum import IntEnum, unique

# A = Rock = 1; B = Paper = 2; C = Scissors = 3
# X -> must lose; Y -> must draw; Z -> must win

# score = shape + wld (wld = 0 for loss, 3 for draw, 6 for win)

scoring_table = {('A', 'A'): 3, ('A', 'B'): 6, ('A', 'C'): 0,
                 ('B', 'A'): 0, ('B', 'B'): 3, ('B', 'C'): 6,
                 ('C', 'A'): 6, ('C', 'B'): 0, ('C', 'C'): 3}

shape_value = {'A': 1, 'B': 2, 'C': 3}

lose = {'A': 'C', 'B': 'A', 'C': 'B'}
draw = {'A': 'A', 'B': 'B', 'C': 'C'}
win = {'A': 'B', 'B': 'C', 'C': 'A'}

response = {'X': lose, 'Y': draw, 'Z': win}

def score(opp, me):
    return scoring_table[(opp, me)] + shape_value[me]


#print(f'(A, X) - expect 4; get {score("A", "X")}')
#print(f'(A, Y) - expect 8; get {score("A", "Y")}')

my_score = 0
with open('strat.txt', 'r') as stratfile:
    for line in stratfile:
        opp, outcome = line.strip().split()
        my_score += score(opp, response[outcome][opp])

print(f'Total score: {my_score}')

