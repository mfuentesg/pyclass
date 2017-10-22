#!/bin/python3
# -*- coding: utf-8 -*-


def encrypt_char(c, k):
    ci = ord(c)
    l = 'Z' if c.isupper() else 'z'
    o = 'A' if c.isupper() else 'a'

    if ci + k > ord(l):
        return chr(ord(o) + (ci + k - ord(l)) - 1)

    return chr(ci + k)

def decrypt_char(c, k):
    ci = ord(c)
    l = 'Z' if c.isupper() else 'z'
    o = 'A' if c.isupper() else 'a'

    if ci - k < ord(o):
        return chr(ord(l) - abs(k - (ci - ord(o))) + 1)

    return chr(ci - k)

def caesar_cipher(text, key, decrypt = False):
    char_action = decrypt_char if decrypt else encrypt_char

    if key < 0:
        raise ValueError('The encryption/decryption key must be greater than 0')

    if key == 0 or key % 26 == 0:
        return text

    K = key % 26 if key > 26 else key
    return ''.join([char_action(x, K) if x.isalpha() else x for x in text])

