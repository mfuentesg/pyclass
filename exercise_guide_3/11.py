#!/bin/python3
# -*- coding: utf-8 -*-

def max_list(l):
    m = l[0]

    for x in l:
        if x > m:
            m = x
    return m

l = [1,1,2,3,4,0,10,-5]
print(max_list(l))
