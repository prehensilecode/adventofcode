#!/usr/bin/env python3
import sys
import copy


class Board:
    def __init__(self, data):
        self.data = copy.deepcopy(data)

    def __repr__(self):
        return f'{self.data}'


lines = []
with open('test.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

calls = [int(x) for x in lines[0].split(',')]
del lines[0:2]

nboards = 0
lines_per_board = 5
board = []
boards = []
nth_line = 1
for line in lines:
    if line:
        print(f'{nth_line} line: {line}')
        board.append([int(c) for c in line.strip().split()])
        if nth_line == 5:
            nboards += 1
            print(f'Board #{nboards}: {board}')
            boards.append(Board(board))
        nth_line += 1
    else:
        print('BLANK')
        nth_line = 1
        del board[:]


print(f'Found {nboards} boards')
print(f'Boards = {boards}')
