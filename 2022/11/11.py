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

    def throw(self, other):
        if type(other) == Monkey:
            for i in self.items:
                other.items.append(i)

    def inspect(self, item):
        old = item
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

            if len(line) == 0:
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


monkeys = read_monkeys('test.txt')

for m in monkeys:
    print(m)

