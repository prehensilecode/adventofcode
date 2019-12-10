#!/usr/bin/env python3
import sys
import os
import argparse

debug_p = True

def check_digits(pw):
    return len(str(pw)) == 6


def check_doubles(pw):
    pwstr = str(pw)
    retval = False

    p = ''
    q = ''
    for i in range(len(pwstr) - 1):
        p = pwstr[i]
        q = pwstr[i+1]
        if p == q:
            retval = True
            break
    return retval


def check_exactly_doubles(pw):
    global debug_p

    pwstr = str(pw)
    retval = False
    
    p = ''
    q = ''
    cnt = []
    grp = 0
    cnt.append(1)
    for i in range(len(pwstr) - 1):
        p = pwstr[i]
        q = pwstr[i+1]
        if p == q:
            cnt[grp] += 1
        else:
            grp += 1
            cnt.append(1)

    if 2 in cnt:
        retval = True

    return retval
            

def check_monotonic(pw):
    pwstr = str(pw)
    retval = True

    for i in range(len(pwstr) - 1):
        if int(pwstr[i]) > int(pwstr[i+1]):
            retval = False
            break
    return retval


def run_tests():
    pws = [112233, 123444, 111122]

    for pw in pws:
        print('pw = {}'.format(pw))
        print('  check_digits(pw) = {}'.format(check_digits(pw)))
        print('  check_doubles(pw) = {}'.format(check_doubles(pw)))
        print('  check_exactly_doubles(pw) = {}'.format(check_exactly_doubles(pw)))
        print('  check_monotonic(pw) = {}'.format(check_monotonic(pw)))
        print('')

    
def main():
    global debug_p

    parser = argparse.ArgumentParser("AoC 4")
    parser.add_argument('limits', metavar='limits', type=int, nargs=2, help='Limits')
    parser.add_argument('-d', '--debug', action='store_true', help='Debug mode')

    args = parser.parse_args()

    if debug_p:
        print(args)
        print(args.limits)
        
        run_tests()

    cnt = 0
    for pw in range(args.limits[0], args.limits[1] + 1):
        if check_digits(pw):
            if check_doubles(pw):
                if check_monotonic(pw):
                    cnt += 1
            
    print('cnt = {}'.format(cnt))

    cnt = 0
    for pw in range(args.limits[0], args.limits[1] + 1):
        if check_digits(pw):
            if check_exactly_doubles(pw):
                if check_monotonic(pw):
                    cnt += 1

    print('cnt = {}'.format(cnt))


if __name__ == '__main__':
    main()

