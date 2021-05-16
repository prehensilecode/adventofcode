#!/usr/bin/env python3
import sys
import os

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
    #print(p)
    if valid_passport(p):
        print('VALID', p)
        n_valid += 1
    else:
        print('INVALID', p)

print(f'{n_valid} valid passports')
