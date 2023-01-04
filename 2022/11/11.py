#!/usr/bin/env python3
import sys
import os
import regex as re

DEBUG = True

class Monkey:
    def __init__(self, index:int, items:list, op:str, test:str, true_action:str, false_action:str):
        self.index = index
        self.items = items
        self.op = op
        self.test = test
        self.true_action = true_action
        self.false_action = false_action

    def throw(self):
        # all tests are "Divisble by N"
        divisor = int(self.test.split()[-1])

        while self.items:
            item = self.items.pop(0)
            if item % divisor:
                other = int(self.true_action.split()[-1])
            else:
                other = int(self.false_action.split()[-1])
            return (item, other)

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

    n_lines = len(lines)
    for i in range(n_lines):
        line = lines[i]
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
for m in monkeys:
    insp = m.inspect()
    if insp:
        no_of_inspections[m.index] += 1
        worry = worry // 3
        item, other_monkey = m.throw()

        if DEBUG:
            print(f'DEBUG: item = {item}, other_monkey = {other_monkey}')

        monkeys[other_monkey].catch(item)
    else:
        continue

    print(f'worry = {worry}')

