#!/usr/bin/env python3
import sys
import os
import re

'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''

# valid passport requires all byr, iyr, eyr, hgt, hcl, ecl, pid, cid.
# cid is OPTIONAL

def valid_passport(passport):
    req_fields = set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
    valid_p = True
    for f in req_fields:
        valid_p = valid_p and (f in passport)
    return valid_p

# byr: 4 digit, [1920, 2002]
# iyr: 4 digit, [2010, 2020]
# eyr: 4 digit, [2020, 2030]
def valid_yr(yr, min, max):
    print('FOOBAR YEAR: ', yr, min, max)
    return (len(yr) == 4) and (int(yr) >= min) and (int(yr) <= max)

def valid_hgt(hgt):
    valid_p = None
    height, unit = int(hgt[:-2]), hgt[-2:]
    print('FOOBAR HEIGHT, UNIT: ', height, unit)
    if unit == 'cm':
        valid_p = (height >= 150) and (height <= 193)
    elif unit == 'in':
        valid_p = (height >= 59) and (height <= 76)

    return valid_p

def valid_hcl(hcl):
    hex_pat = re.compile(r'([0-9a-fA-F]{6})')
    print('FOOBAR HAIR: ', re.match(hex_pat, hcl[1:]))
    return (hcl[0] == '#') and (re.match(hex_pat, hcl[1:]))

def valid_ecl(ecl):
    print('FOOBAR EYE COLOR:', ecl)
    return ecl in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def valid_pid(pid):
    print('FOOBAR PID:', pid)
    return re.match(r'(\d{9})', pid)

def strict_valid_passport(p):
    if valid_passport(p):
        print('LOOSE VALID')
        return valid_yr(p['byr'], 1920, 2002) and valid_yr(p['iyr'], 2010, 2020) and valid_yr(p['eyr'], 2020, 2030) and valid_hgt(p['hgt']) and valid_hcl(p['hcl']) and valid_ecl(p['ecl']) and valid_pid(p['pid'])
    else:
        print('LOOSE INVALID')
        return False


def parse_pp(lines):
    pp = {}
    for l in lines:
        for el in l.split(' '):
            field, val = el.split(':')
            if field == 'byr' or field == 'iyr' or field == 'eyr' or field == 'pid' or field == 'cid':
                pp[field] = int(val)
            else:
                pp[field] = val

def read_passports(filename):
    passports = []
    with open(filename, 'r') as f:
        p = {}
        for line in f:
            if line.strip() == '':
                #print('BLANK')
                #print('p = ', f'{p}')
                passports.append(p.copy())
                p = {}
            else:
                #print(line.strip())
                data_line = line.strip().split(' ')
                for item in data_line: 
                    #print(item)
                    k, v = item.split(':')
                    p[k] = v

    return passports

passports = read_passports('input04')

print('Read {} passports'.format(len(passports)))
n_valid = 0
for p in passports:
    if valid_passport(p):
        #print('VALID', p)
        n_valid += 1
    else:
        #print('INVALID', p)
        pass

print(f'{n_valid} valid passports')
print('')

n_valid = 0
for p in passports:
    if strict_valid_passport(p):
        print('VALID', p)
        n_valid += 1
    else:
        print('INVALID', p)

print(f'{n_valid} strictly valid passports')
