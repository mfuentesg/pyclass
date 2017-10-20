#!/bin/python3
# -*- coding: utf-8 -*-

def power(n, m):
    p = 1
    for _ in range(m):
        p = p * n
    return p

n = int(input("enter the number: "))
m = int(input("enter the power: "))

print(power(n,m))

