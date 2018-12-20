#!/usr/bin/env python3.5
import sys
import os
import re
import collections

def is_nice_p(s):
    # needs at least 2 occurences of a pair
    has_two_pairs_p = False
    dbl_pat = re.compile(r'([a-z]{2}).*\1')
    if dbl_pat.search(s):
        print(dbl_pat.search(s).group(0))
        has_two_pairs_p = True

    # a repeated char, interposed by one char
    has_triplet_p = False
    triplet_pat = re.compile(r'([a-z])[a-z]\1')
    if triplet_pat.search(s):
        print(triplet_pat.search(s).group(0))
        has_triplet_p = True

    return (has_two_pairs_p and has_triplet_p)

def count_nice(strs):
    count = 0
    for s in strs:
        if is_nice_p(s):
            count += 1
    return count

if __name__ == '__main__':
    strs = []
    with open('input.txt', 'r') as f:
        for l in f:
            strs.append(l)

    print(count_nice(strs))

