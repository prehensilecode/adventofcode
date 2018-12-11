#!/usr/bin/env python3
import sys
import os

def metric(s1, s2):
    # return no. of characters different

    k = [(s1[i] != s2[i]) for i in range(len(s1))]

    return sum(k)


def samepart(s1, s2):
    ret = []
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            ret.append(s1[i])
    return ''.join(ret)


def find_two_boxes(idlist):
    ret = None
    nids = len(idlist)
    for i in range(nids):
        for j in range(nids):
            #print("BAR: i = {}, j = {}".format(i, j))
            #print("BAR: idlist[{}] = {}, idlist[{}] = {}".format(i, idlist[i], j, idlist[j]))
            if (i != j) and (len(idlist[i]) == len(idlist[j])) and (metric(idlist[i], idlist[j]) == 1):
                ret = samepart(idlist[i], idlist[j])
                break

    return ret
            

if __name__ == '__main__':
    idlist = []
    with open('input.txt', 'r') as f:
        for l in f:
            idlist.append(l.strip())


    #print(samepart("abcde", "abxde"))
    print(find_two_boxes(idlist))

