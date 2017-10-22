#!/bin/python3
# -*- coding: utf-8 -*-

from caesar_cipher import caesar_cipher


def test(base, expected):
    result = "SUCCESS" if base == expected else "FAILED"
    print("Case {} == {} -> {}".format(base, expected, result))

print(" cipher ".center(20, '='))
test(caesar_cipher('¡hola!', 2), '¡jqnc!')
test(caesar_cipher('pyclass', 0), 'pyclass')
test(caesar_cipher('zapato', 2), 'bcrcvq')
test(caesar_cipher('water', 3), 'zdwhu')
test(caesar_cipher('hi', 53), 'ij')
test(caesar_cipher('middle-Outz', 2), 'okffng-Qwvb')
test(caesar_cipher('Hello_World!', 4), 'Lipps_Asvph!')
print("decipher".center(20, '='))
test(caesar_cipher('¡jqnc!', 2, decrypt=True), '¡hola!')
test(caesar_cipher('pyclass', 0, decrypt=True), 'pyclass')
test(caesar_cipher('bcrcvq', 2, decrypt=True), 'zapato')
test(caesar_cipher('zdwhu', 3, decrypt=True), 'water')
test(caesar_cipher('ij', 53, decrypt=True), 'hi')
