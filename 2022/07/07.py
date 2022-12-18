#!/usr/bin/env python3
import sys
import os

from enum import Enum

class NodeType(Enum):
    DIR = 1
    FILE = 2

class Node:
    def __init__(self, name=None, nodetype=NodeType.FILE, size=0):
        self.name = name
        self.nodetype = nodetype
        self.size = size
        self.children = []

    def __repr__(self):
        retstr = f'{self.name} - {self.nodetype}\n'

        for c in self.children:
            depth = 1
            if c.nodetype == NodeType.FILE:
                retstr += f'{"    "*depth}{c.name} - {c.nodetype} - {c.size}\n'
            elif c.nodetype == NodeType.DIR:
                retstr += f'{"    "*depth}{c.name} - {c.nodetype}\n'
                retstr += c.__repr__()

        return retstr

    def add_child(self, name=None, nodetype=None):
        if self.nodetype == NodeType.FILE:
            print(f'ERROR: cannot add child to {self.nodetype}')
            sys.exit(69)
        else:
            self.children.append(Node(name, nodetype))



def parse_listing(line):
    left, right = line.split()

    if left == 'dir':
        return Node(name=right, nodetype=NodeType.DIR)
    else:
        return Node(name=right, nodetype=NodeType.FILE, size=int(left))


def parse_log(log):
    dir_tree = None
    for i in range(len(log)):
        l = log[i]
        if l[0] == '$':
            cmd = l[2:]
            if cmd[:2] == 'cd':
                dirname = cmd[3:]
                if dirname == '/':
                    dir_tree = Node(name=dirname, nodetype=NodeType.DIR)
                elif dirname == '..':
                    # FIXME
                    pass
                else:
                    dir_tree.add_child(name=dirname, nodetype=NodeType.DIR)
            elif cmd[:2] == 'ls':
                i += 1
                dir_tree.add_child(parse_listing(log[i]))

        i += 1

    return dir_tree


n = Node('foo', NodeType.DIR)
print(n)


log = []
with open('test.txt', 'r') as infile:
    for line in infile:
        log.append(line.strip())

dir_tree = parse_log(log)
print(dir_tree)
