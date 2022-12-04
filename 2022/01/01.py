#!/usr/bin/env python3
import sys, os

elves = []
elves.append([])
with open('input_01.txt', 'r') as infile:
    elf_count = 0
    elves[elf_count] = []
    for line in infile:
        if len(line.strip()):
            elves[elf_count].append(int(line.strip()))
        else:
            # next elf
            elf_count += 1
            elves.append([])
            continue

total_cals = []
for elf in elves:
    total_cals.append(sum(elf))

print(f'Part 1: {max(total_cals)}')

total_cals.sort(reverse=True)
print(f'Part 2: {sum(total_cals[:3])}')
