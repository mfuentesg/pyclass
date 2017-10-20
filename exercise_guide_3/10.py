#!/bin/python3
# -*- coding: utf-8 -*-

def print_pattern(L):
    for x in range(1, L+1):
        print(' ' * (L - x) + '#' * x)

print_pattern(int(input('enter a length: ')))
