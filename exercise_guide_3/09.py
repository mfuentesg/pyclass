#!/bin/python3
# -*- coding: utf-8 -*-

def sum_list(l):
    s = 0
    for x in l:
        s += x
    return s

l = [1,2,3]
print(sum_list(l))
#print(sum(l))
