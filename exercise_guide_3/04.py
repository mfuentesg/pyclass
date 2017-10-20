#!/bin/python3
# -*- coding: utf-8 -*-

t = input("enter the text: ")
c = input("enter the character: ")

if len(c) == 0:
    print("Espera, no puedo realizar la búsqueda sin algo que buscar")
elif c in t:
    print("Encontré el caractér {}, en el texto {}".format(c, t))
else:
    print("NO Encontré el caractér {}, en el texto {}".format(c, t))
