#!/usr/bin/env python3
import sys
import os


answers = []
with open('input06', 'r') as f:
    group = []
    for line in f:
        if line.strip() == '':
            answers.append(group.copy())
            group = []
        else:
            group.append(line.strip())

#print(answers)

unique_answers = []
for group in answers:
    u_group = set()
    for e in group:
        ans = set(list(e))
        u_group |= ans
    unique_answers.append(u_group.copy())
    u_group = []

#print(unique_answers)
sum = 0
for u in unique_answers:
    sum += len(u)

print(sum)

