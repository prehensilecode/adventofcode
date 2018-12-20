#!/usr/bin/env python3.5
import sys
import os
import re
import collections

def is_nice_p(s):
    # needs 3 or more vowels
    c = collections.Counter(s)
    has_vowels_p = ((c['a'] + c['e'] + c['i'] + c['o'] + c['u']) > 2)

    # needs at least one repeated letter
    has_repeated_letter_p = False
    dbl_pat = re.compile(r'([a-z])\1')
    if dbl_pat.search(s):
        has_repeated_letter_p = True

    # exclude ab, cd, pq, or xy
    no_bad_p = True
    if re.search(r'ab', s) or re.search(r'cd', s) or re.search(r'pq', s) or re.search(r'xy', s):
        no_bad_p = False

    return (has_vowels_p and has_repeated_letter_p and no_bad_p)

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

