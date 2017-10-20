#!/bin/python3
# -*- coding: utf-8 -*-

def best_student(students):
    return max(students, key=lambda student: student[1])

students=[
    ('Kevin',6.0),
    ('Andrés',6.01),
    ('Benito',7.0),
    ('Marcelo', 7.1)
]

student, grade = best_student(students)
print('{} eres el mejor alumno, tu nota es {}'.format(student, grade))
