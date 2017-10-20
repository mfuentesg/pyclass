#!/bin/python3
# -*- coding: utf-8 -*-

n = int(input("enter the number: "))

# range(2, n) -> [2, n-1]
for x in range(2, n):
    if n % x == 0:
        print(x, end=" ")
print()
