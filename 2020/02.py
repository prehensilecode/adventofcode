#!/usr/bin/env python3
import sys
import os

def count_char(char, pw):
    count = 0
    for c in sorted(pw):
        if c == char:
            count += 1
    return count


def check_pw(pos, char, pw):
    return (pw[pos[0]-1] == char and pw[pos[1]-1] != char) or (pw[pos[0]-1] != char and pw[pos[1]-1] == char)

pol_pas = []
with open('input02', 'r') as f:
    for l in f:
        pol_pas.append([el.strip() for el in l.split(':')])

num_valid = 0
for e in pol_pas:
    rep = [int(i) for i in e[0].split(' ')[0].split('-')]
    char = e[0].split(' ')[-1]
    pw = e[1]

    #print(rep, char, pw)
    count = count_char(char, pw)
    #print(count)
    if count >= rep[0] and count <= rep[1]:
        num_valid += 1

print(num_valid)

num_valid = 0
for e in pol_pas:
    pos = [int(i) for i in e[0].split(' ')[0].split('-')]
    char = e[0].split(' ')[-1]
    pw = e[1]
    if check_pw(pos, char, pw):
        num_valid += 1

print(num_valid)
