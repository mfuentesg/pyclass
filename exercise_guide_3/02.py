#!/bin/python3
# -*- coding: utf-8 -*-

def fahrenheit(g):
    return (9/5 * g) + 32

g = int(input("enter the temperature: "))
print('{} F'.format(fahrenheit(g)))
