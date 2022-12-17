#!/usr/bin/env python3
import sys
import os

from enum import Enum

class NodeType(Enum):
    DIR = 1
    FILE = 2

class Node:
    def __init__(self, name=None, nodetype=NodeType.FILE):
        self.name = name
        self.nodetype = nodetype
        self.children = None

    def __repr__(self):
        return f'{self.name} - {self.nodetype}'



n = Node('foo', NodeType.DIR)
print(n)
