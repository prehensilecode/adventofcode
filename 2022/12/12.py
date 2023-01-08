#!/usr/bin/env python3
import sys
import os

with open('test.txt', 'r') as f:
    for line in f:
        print(line.strip())
