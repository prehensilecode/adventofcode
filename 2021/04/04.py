#!/usr/bin/env python3
import sys
import copy


class Board:
    def __init__(self, data):
        self.data = copy.deepcopy(data)

    def index(self, number):
        r = 0
        row_ind = 0
        col_ind = 0
        for row in self.data:
            if number in row:
                print(f'DEBUG: r = {r} - row = {row}')
                row_ind = r
                col_ind = row.index(number)
                break
            r += 1
        return (row_ind, col_ind)

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
print('')

# expect (0, 0)
print(f'index of 22 in boards[0] = {boards[0].index(22)}')
print('')

# expect (3, 1)
print(f'index of 11 in boards[1] = {boards[1].index(11)}')
print('')

# expect (1, 3)
print(f'index of 9 in boards[2] = {boards[2].index(9)}')
print('')
