#!/usr/bin/env python3
import sys
import os
import re
from anytree import Node, NodeMixin, RenderTree, Walker
from anytree.exporter import DotExporter

debug_p = True

class Directory(NodeMixin):
    def __init__(self, name, parent=None, children=None):
        self.name = name
        self.parent = parent
        if children:
            self.children = children


class File(NodeMixin):
    def __init__(self, name, size, parent=None, children=None):
        self.name = name
        self.size = size
        self.parent = parent
        if children:
            self.children = children

    def __repr__(self):
        return f'file "{self.name}", size={self.size}'


def parse_listing(line):
    left, right = line.split()

    if left == 'dir':
        return Node(right)
    else:
        return Node(right)


def parse_log(log):
    global debug_p


    myvars = vars()
    walker = Walker()
    curdir = None
    root = None
    for i in range(len(log)):
        l = log[i]
        if debug_p:
            print(f'DEBUG: l = {l}')
            if curdir:
                print(f'DEBUG: curdir = {curdir.name}')
            else:
                print(f'DEBUG: curdir = {curdir}')

        if l[0] == '$':
            cmd = l[2:]
            if debug_p:
                print(f'DEBUG: cmd = {cmd}')

            if cmd[:2] == 'cd':
                dirname = cmd[3:]
                if dirname == '/':
                    root = Directory(dirname)
                    curdir = root
                else:
                    if dirname == '..':
                        if curdir:
                            curdir = curdir.parent
                        else:
                            print(f'ERROR: curdir = {curdir}')
                            sys.exit(3)
                    else:
                        myvars[dirname] = Directory(dirname, parent=curdir)
                        curdir = myvars[dirname]
            elif cmd[:2] == 'ls':
                continue
        else:
            if l[:3] == 'dir':
                dirname = l[4:]
            elif re.match(r'[0-9]', l[0]):
                filesize = int(l.split()[0])
                filename = l.split()[1]
                myvars[filename] = File(filename, filesize, parent=curdir)

                if debug_p:
                    print(f'DEBUG: file = {myvars[filename]}')

        i += 1

    return root


log = []
with open('test.txt', 'r') as infile:
    for line in infile:
        log.append(line.strip())

dir_tree = parse_log(log)

print()
for pre, fill, node in RenderTree(dir_tree):
    print(f'{pre}{node.name}')

