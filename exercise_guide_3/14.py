#!/bin/python3
# -*- coding: utf-8 -*-

def people_average(p):
    return [(x['name'], sum(x['salaries']) / len(x['salaries'])) for x in p]

people = [
    {'name':'Kevin','salaries':[100,99,101]},
    {'name':'Andrés','salaries':[98,120]}
]

for p in people_average(people):
    name, avg = p
    print('{} => {}'.format(name, avg))
