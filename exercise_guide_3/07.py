#!/bin/python3
# -*- coding: utf-8 -*-

def factorial(n):
    f = 1
    for x in range(1, n + 1):
        f = f * x
    return f

n = int(input("enter the number: "))
print(factorial(n))
