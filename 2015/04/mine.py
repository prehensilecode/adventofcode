#!/usr/bin/env python3.5
import sys 
import os
import hashlib

secret = 'yzbqklnj'

def mine(secret):
    hash = 'aaaaaa'

    i = 0
    while len(hash) > 5 and hash[0:6] != '000000':
        i += 1
        arg = ''.join([secret, str(i)])
        hash = hashlib.md5(arg.encode()).hexdigest()
    
    print(i, hash)

if __name__ == '__main__':
    mine(secret)

