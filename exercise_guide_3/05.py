#!/bin/python3
# -*- coding: utf-8 -*-

def reverse(w):
    rw = ''
    for n in range(len(w)):
        rw = w[n] + rw
    return rw

print(reverse(input("enter the text to reverse: ")))
