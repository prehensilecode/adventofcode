#!/usr/bin/env python3
from BitVector import BitVector

def gamma_epsilon(loglines):
    res = []
    nlines = len(loglines)
    npos = len(loglines[0])
    print(f'nlines = {nlines}')
    print(f'npos = {npos}')
    s = 0
    for n in range(npos):
        for l in loglines:
            s += int(l[n])
        if s < nlines/2.:
            res.append('0')
        else:
            res.append('1')
        s = 0

    gamma_bin = ''.join(res)
    epsilon_bin = []
    for b in res:
        if b == '0':
            epsilon_bin.append('1')
        else:
            epsilon_bin.append('0')
    return int(''.join(gamma_bin), 2), int(''.join(epsilon_bin), 2)


def dg(loglines):
    data = []
    for line in loglines:
        data.append(BitVector(bitstring=line.strip()))

    nlines = len(data)
    npos = len(loglines[0])

    # list of 0th elems
    res = []
    for n in range(npos):
        nths = [int(el[n]) for el in data]
        if sum(nths) < nlines/2.:
            res.append(0)
        else:
            res.append(1)
    gamma_bin = BitVector(bitlist=res)
    epsilon_bin = ~gamma_bin

    return gamma_bin.int_val(), epsilon_bin.int_val()


loglines = []
with open('test1.txt', 'r') as f:
    for l in f:
        loglines.append(l.strip())

g, e = gamma_epsilon(loglines)
print(f'g, e = {g}, {e}')
power = g * e
print(f'Power = {power}')
print('')

print('Using BitVector')
g, e = dg(loglines)
print(f'g, e = {g}, {e}')
print(f'Power = {g *  e}')
