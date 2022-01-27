#!/usr/bin/env python3
import sys
import copy

class Board:
    def __init__(self, data):
        self.data = copy.deepcopy(data)
        self.marks = []
        self.__init_marks()

    def __init_marks(self):
        for i in range(5):
            self.marks.append(5 * [0])
        print(f'DEBUG: self.marks = {self.marks}')

    def index(self, number):
        r = 0
        row_ind = 0
        col_ind = 0
        for row in self.data:
            if number in row:
                # print(f'DEBUG: r = {r} - row = {row}')
                row_ind = r
                col_ind = row.index(number)
                break
            r += 1
        return (row_ind, col_ind)

    def mark(self, number):
        b_p = False
        mark_ind = self.index(number)
        print(f'mark_ind = {mark_ind}')
        self.marks[mark_ind[0]][mark_ind[1]] = 1
        if self.bingo_p():
            print('BINGO!')
            b_p = True
        return b_p

    def bingo_p(self):
        # bingo is a full row or column marked
        retval = False
        for row in self.marks:
            if sum(row) == 5:
                retval = True
                break
        cols = []
        for i in range(5):
            cols.append(5 * [0])
        col_ind = 0
        for row_ind in range(5):
            for col_ind in range(5):
                #print(f'row_ind = {row_ind}; col_ind = {col_ind}')
                cols[col_ind][row_ind] = self.marks[row_ind][col_ind]
        #print(f'DEBUG: cols = {cols}')
        for col in cols:
            if sum(col) == 5:
                retval = True
                break
        return retval

    def __repr__(self):
        return f'Board = {self.data}; marks = {self.marks}'


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
        #print(f'{nth_line} line: {line}')
        board.append([int(c) for c in line.strip().split()])
        if nth_line == 5:
            nboards += 1
            #print(f'Board #{nboards}: {board}')
            boards.append(Board(board))
        nth_line += 1
    else:
        #print('BLANK')
        nth_line = 1
        del board[:]

for b in boards:
    for c in calls:
        print(f'Call = {c}')
        if b.mark(c):
            break

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
