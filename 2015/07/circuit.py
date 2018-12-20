#!/usr/bin/env python3.5
import sys
import os
import re

def circuit(instr):
    numpat = re.compile(r'(\d+)')
    letpat = re.compile(r'([a-z]+)')

    symbols = {}

    #for i in instr:
    #    oper, dest = i.split('->')
    #    oper = oper.strip()
    #    dest = dest.strip()
    #    symbols[dest] = 0


    for i in sorted(instr):
        oper, dest = i.split('->')
        oper = oper.strip()
        dest = dest.strip()
        opspl = oper.split(' ')
        if len(opspl) == 1:
            # assignment
            if numpat.match(opspl[0]):
                symbols[dest] = int(opspl[0])
            else:
                if opspl[0] in symbols:
                    symbols[dest] = symbols[opspl[0]]
        elif len(opspl) == 2:
            # NOT
            if opspl[1] in symbols:
                symbols[opspl[1]] = ~symbols[opspl[1]]
        elif len(opspl) == 3:
            # binary operation
            # a OP b
            a, o, b = opspl

            if numpat.match(a): 
                a = int(a)
            else:
                if a in symbols:
                    a = symbols[a]
                else:
                    continue

            if numpat.match(b): 
                b = int(b)
            else:
                if b in symbols:
                    b = symbols[b]
                else:
                    continue

            if o == 'AND':
                symbols[dest] = a & b
            elif o == 'OR':
                symbols[dest] = a | b
            elif o == 'LSHIFT':
                symbols[dest] = a << b
            elif o == 'RSHIFT':
                symbols[dest] = a >> b



    print('symbols = {}'.format(symbols))
    #print('a = {}'.format(symbols['a']))

if __name__ == '__main__':
    instr = []
    with open('test.txt', 'r') as f:
        for l in f:
            instr.append(l.strip())

    circuit(instr)

