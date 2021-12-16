#!/usr/bin/env python3

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
        if s < float(nlines)/2.:
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


loglines = []
with open('input1.txt', 'r') as f:
    for l in f:
        loglines.append(l.strip())

ge = gamma_epsilon(loglines)
print(ge)
power = ge[0] * ge[1]
print(f'Power = {power}')

