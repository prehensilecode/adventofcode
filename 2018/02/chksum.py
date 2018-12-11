#!/usr/bin/env python3
import sys
import os

def chksum(idlist):
    num_duplets = count_duplets(idlist)
    num_triplets = count_triplets(idlist)

    print("no. duplets  = {}".format(num_duplets))
    print("no. triplets = {}".format(num_triplets))

    return (num_duplets * num_triplets)

def count_duplets(idlist):
    ndup = 0
    for id in idlist:
        s = set(list(id))
        for e in s:
            c = id.count(e)
            if c == 2:
                ndup += 1
                break
    return ndup

def count_triplets(idlist):
    ntrip = 0
    for id in idlist:
        s = set(list(id))
        for e in s:
            c = id.count(e)
            if c == 3:
                ntrip += 1
                break
    return ntrip

if __name__ == '__main__':
    idlist = []
    with open('input.txt', 'r') as f:
        for l in f:
            idlist.append(l.strip())

    print(chksum(idlist))

