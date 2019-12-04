#!/usr/bin/env python3
import sys
import os
import re

def parse_input(fn):
    timestamp_pat = re.compile(r'^[.*]\ ')

    with open(fn, 'r') as f:
        lines = f.readlines()
        for l in lines:
            print(l.strip())

if __name__ == '__main__':
    parse_input('input.txt')

