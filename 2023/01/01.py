#!/usr/bin/env python
import sys
import os
import re
from collections import OrderedDict

with open('input.txt', 'r') as f:
    sum = 0
    numstr = ''
    for l in f:
        for c in l:
            if c.isdigit():
                numstr += c

        sum += int(numstr[0] + numstr[-1])
        numstr = ''

print(f'Sum = {sum}')

spelled_numbers = ('zero', 'one', 'two', 'three',
                   'four', 'five', 'six',
                   'seven', 'eight', 'nine')
numbers = range(11)

num_pats = set()
for sn in spelled_numbers:
    num_pats.add(re.compile(f'{sn}'))


pat_dict = dict(zip(spelled_numbers, numbers))

for k, v in pat_dict.items():
    print(k, v)
print()

#pat_dict.move_to_end('zero')
#
#for k, v in pat_dict.items():
#    print(k, v)

sys.exit(0)

with open('test2.txt', 'r') as f:
    sum = 0
    numstr = ''
    for line in f:
        line_check = line.strip()
        for np in num_pats:
            print(f'Looking for {np} in {line_check}')
            if np.search(line_check.strip()):
                print(f'... found {np} in {line.strip()}')
                numstr += f'{pat_dict[np.pattern]}'
                print(f'DEBUG: numstr = {numstr}')
        if len(numstr) > 0:
           sum += int(numstr[0] + numstr[-1])
        numstr = ''

print()
print(f'TEST: expect 281')
print(f'Sum_2 = {sum}')

