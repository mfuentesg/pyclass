#!/bin/python3
# -*- coding: utf-8 -*-

def vowel_counter(w):
    vowels = ('a', 'e', 'i', 'o', 'u')
    counter = 0

    for v in w:
        if v in vowels:
            counter = counter + 1
    return counter

print(vowel_counter(input('enter a text: ')))
