#!/usr/bin/env python3
import sys
import os

def unique_answers(answers):
    ua = []

    for group in answers:
        u_group = set()
        for e in group:
            ans = set(list(e))
            u_group |= ans
        ua.append(u_group.copy())
        u_group = []

    return ua

def part_one(ua):
    sum = 0
    for u in ua:
        sum += len(u)

    print('Part 1:', sum)


def answer_by_everyone(a, u):
    retval = True
    for i in a:
        #print('u = {} ; i = {} ; u in i = {}'.format(u, i, u in i))
        retval = retval and (u in i)
    #print('')
    return retval

def part_two(answers, ua):
    #print('answers =', answers)
    #print('ua =', ua)
    #print('')

    a_ua = [(answers[i], ua[i]) for i in range(len(answers))]

    sum = 0
    for pair in a_ua:
        #print('PAIR:', pair, len(pair[1]))
        for u in pair[1]:
            if answer_by_everyone(pair[0], u):
                #print('adding...')
                #print('')
                sum += 1

    print('Part 2:', sum)


if __name__ == '__main__':
    answers = []
    with open('input06', 'r') as f:
        group = []
        for line in f:
            if line.strip() == '':
                answers.append(group.copy())
                group = []
            else:
                group.append(line.strip())

    ua = unique_answers(answers)

    part_one(ua)

    part_two(answers, ua)
