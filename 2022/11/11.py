#!/usr/bin/env python3
import sys
import os
import regex as re
from functools import reduce

DEBUG = True

class Monkey:
    def __init__(self, index:int, items:list, op:str, test:str, true_action:str, false_action:str):
        self.index = index
        self.items = items
        self.op = op
        self.test = test
        self.true_action = true_action
        self.false_action = false_action

    def throw_maybe(self, worry: int):
        _ = self.items.pop(0)
        print(f'DEBUG: test_worry({worry} = {self.test_worry(worry)})')
        if self.test_worry(worry):
            other = int(self.true_action.split()[-1])
        else:
            other = int(self.false_action.split()[-1])
        return other

    def catch(self, item):
        self.items.append(item)

    def inspect(self):
        if not self.items:
            return None
        else:
            # inspect first item
            old = self.items[0]
            lcls = locals()
            exec(self.op, globals(), lcls)
            new = lcls['new']
            return new

    def test_worry(self, worry: int):
        # all tests are "Divisble by N"
        divisor = int(self.test.split()[-1])
        print(f'DEBUG: Monkey.test_worry(): worry = {worry}, divisor = {divisor}')

        return (worry % divisor) == 0

    def __repr__(self):
        return f'{self.index}, {self.items}, {self.op}, {self.test}, {self.true_action}, {self.false_action}'


def read_monkeys(filename):
    global DEBUG

    monkeys = []

    monkey_pat = re.compile(r'Monkey\ (\d):$')
    items_pat = re.compile(r'Starting\ items:\ (.*)$')
    op_pat = re.compile(r'Operation:\ (.*)$')
    test_pat = re.compile(r'Test:\ (.*)$')
    true_pat = re.compile(r'If true:\ (.*)$')
    false_pat = re.compile(r'If false:\ (.*)$')

    lines = []
    with open(filename) as infile:
        index = 0
        items = []
        op = ''
        test = ''
        true_action = ''
        false_action = ''
        for l in infile:
            line = l.strip()
            print(f'ALOHA: line = {line}')
            lines.append(line)
    # take care of missing empty line at end of file
    lines.append('')

    n_lines = len(lines)
    for i in range(n_lines):
        line = lines[i]
        print(f'WTF: line = {line}')
        if (len(line) == 0) or (i == n_lines - 1):
            print('FOO', index, items, op, test)
            monkeys.append(Monkey(index, items, op, test, true_action, false_action))
        elif monkey_pat.match(line):
            index = int(monkey_pat.match(line).group(1))
            print(f'BAR index = {index}')
        elif items_pat.match(line):
            items = [int(i) for i in items_pat.match(line).group(1).split(',')]
            print(f'BAR items = {items}')
        elif op_pat.match(line):
            op = op_pat.match(line).group(1)
            print(f'BAR op = {op}')
        elif test_pat.match(line):
            test = test_pat.match(line).group(1)
            print(f'BAR test = {test}')
        elif true_pat.match(line):
            true_action = true_pat.match(line).group(1)
            print(f'BAR true_action = {true_action}')
        elif false_pat.match(line):
            false_action = false_pat.match(line).group(1)
            print(f'BAR false_action = {false_action}')
            print()


    return monkeys

worry = 0

monkeys = read_monkeys('input.txt')

n_monkeys = len(monkeys)

no_of_inspections = [0 for i in range(n_monkeys)]

if DEBUG:
    print(f'DEBUG: no. of monkeys = {len(monkeys)} (should be 8)')
    for m in monkeys:
        print(m)
    print()

# FIXME
# 20 rounds
for r in range(20):
    print(f'ROUND {r}')
    for m in monkeys:
        print(f'DEBUG: MONKEY {m.index}')
        print(f'DEBUG:    {m}')
        while m.items:
            print(f'DEBUG: m.items = {m.items}')
            worry = m.inspect()
            if worry:
                no_of_inspections[m.index] += 1
                worry = worry // 3

                if DEBUG:
                    print(f'DEBUG: worry = {worry}')

                other_monkey = m.throw_maybe(worry)

                if DEBUG:
                    print(f'DEBUG: worry = {worry}, other_monkey = {other_monkey}')

                monkeys[other_monkey].catch(worry)
            else:
                continue
            worry = 0
            print()
        print()

    for m in monkeys:
        print(m)

print()
print(f'No. of inspections: {no_of_inspections}')


print(reduce((lambda x, y: x*y), sorted(no_of_inspections, reverse=True)[:2]))
