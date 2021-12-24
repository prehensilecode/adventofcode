#!/usr/bin/env python3
import sys
from BitVector import BitVector

debug_p = False

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


def logdata(loglines):
    data = []
    for line in loglines:
        data.append(BitVector(bitstring=line.strip()))

    return data


def dg(data):
    nlines = len(data)
    npos = len(data[0])

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


def most_common_bits(lines):
    nlines = len(lines)
    npos = len(lines[0])
    retval = []
    for n in range(npos):
        nths = [int(el[n]) for el in lines]
        if sum(nths) < nlines/2.:
            retval.append(0)
        else:
            retval.append(1)

    return BitVector(bitlist=retval)


def og(data):
    global debug_p
    # determine most common value in current bit position;
    # keep only numbers with that bit in that position
    npos = len(data[0])
    kept = []
    for n in range(npos):
        if n == 0:
            mcb = most_common_bits(data)
            for line in data:
                if line[n] == mcb[n]:
                    kept.append(line)

            if debug_p:
                print(f'{[str(x) for x in kept]}')
        else:
            if len(kept) == 1:
                break
            else:
                mcb = most_common_bits(kept)
                kept[:] = [x for x in kept if x[n] == mcb[n]]

                if debug_p:
                    print(f'{[str(x) for x in kept]}')

    if len(kept) != 1:
        print(f'ERROR: len(kept) = {len(kept)}')
        sys.exit(1)

    if debug_p:
        print(f'DEBUG: kept[0] = {kept[0]}')

    return int(kept[0])


def co2(data):
    global debug_p

    npos = len(data[0])
    kept = []
    for n in range(npos):
        if n == 0:
            mcb = most_common_bits(data)
            for line in data:
                if line[n] != mcb[n]:
                    kept.append(line)

            if debug_p:
                print(f'{[str(x) for x in kept]}')
        else:
            if len(kept) == 1:
                break
            else:
                mcb = most_common_bits(kept)
                kept[:] = [x for x in kept if x[n] != mcb[n]]

                if debug_p:
                    print(f'{[str(x) for x in kept]}')

    if len(kept) != 1:
        print(f'ERROR: len(kept) = {len(kept)}')
        sys.exit(1)

    if debug_p:
        print(f'DEBUG: kept[0] = {kept[0]}')

    return int(kept[0])


def life_support(data):
    return og(data) * co2(data)


loglines = []
with open('input1.txt', 'r') as f:
    for line in f:
        loglines.append(line.strip())

# g, e = gamma_epsilon(loglines)
# print(f'g, e = {g}, {e}')
# power = g * e
# print(f'Power = {power}')
# print('')

print('Using BitVector')
data = logdata(loglines)
g, e = dg(data)
print(f'g, e = {g}, {e}')
print(f'Power = {g *  e}')

ogr = og(data)
print(f'Oxygen generator rating = {ogr}')

co2r = co2(data)
print(f'CO2 scrubber rating = {co2r}')

ls = life_support(data)
print(f'Life support rating = {ls}')
