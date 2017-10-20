#!/bin/python3
# -*- coding: utf-8 -*-

def is_palindrome(w):
    ls = 0
    rs = len(w) - 1

    while ls < rs:
        if w[ls] != w[rs]:
            return False

        ls = ls + 1
        rs = rs - 1

    return True

w = input("enter the word to evaluate: ")

if is_palindrome(w):
    print("The word {} is palindrome".format(w))
else:
    print("The word {} is not palindrome".format(w))

