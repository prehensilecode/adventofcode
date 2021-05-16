#!/usr/bin/env python3
import sys
import os

numbers = []
with open('input01', 'r') as f:
    for l in f:
        numbers.append(int(l.strip()))

count = 0
for count in range(len(numbers)):
    for m in numbers[count+1:]:
        if numbers[count] + m == 2020:
            print(numbers[count] * m)

count = 0
for count in range(len(numbers)):
    for m in numbers[count+1:]:
        for n in numbers[count+2:]:
            if numbers[count] + m + n == 2020:
                print(numbers[count] * m * n)
