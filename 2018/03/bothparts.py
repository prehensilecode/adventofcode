#!/usr/bin/env python3
import sys
import os

fabricmap = []

def map_claims(claims):
    global fabricmap

    for c in claims:
        for i in range(c[0][0], c[0][0]+c[1][0]):
            for j in range(c[0][1], c[0][1]+c[1][1]):
                fabricmap[i][j] += 1


def two_or_more_claims():
    global fabricmap

    s = 0
    for row in fabricmap:
        for el in row:
            if el > 1:
                s += 1

    return s


def sum_map():
    global fabricmap

    s = 0
    for row in fabricmap:
        s += sum(row)

    return s


def check_claim(c):
    global fabricmap

    solo_p = True

    for i in range(c[0][0], c[0][0]+c[1][0]):
        for j in range(c[0][1], c[0][1]+c[1][1]):
            if fabricmap[i][j] != 1:
                solo_p = False
                break

    return solo_p


def solo_claim(claims):
    global fabricmap

    found = False
    clid = 0
    while not found:
        for c in claims:
            clid += 1
            if not check_claim(c):
                continue
            else:
                found = True
                break

    return clid


if __name__ == '__main__':
    # init. fabricmap
    fabricmap = [[0 for i in range(1000)] for j in range(1000)]
            
    claims = []
    with open('input.txt', 'r') as f:
        for l in f:
            claiminfo = l.strip().split()
            tmp1 = claiminfo[2].split(':')[0].split(',')
            origin = (int(tmp1[0]), int(tmp1[1]))
            tmp2 = claiminfo[3].strip().split('x')
            area = (int(tmp2[0]), int(tmp2[1]))
            claims.append((origin, area))

    map_claims(claims)

    print("sum(fabricmap) = {}".format(sum_map()))
    print("two or more = {}".format(two_or_more_claims()))

    print("solo claim = {}".format(solo_claim(claims)))
