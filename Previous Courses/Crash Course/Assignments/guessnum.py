# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:24:44 2018

@author: nelson
"""


import random
n = random.randrange(1, 101)
print("I've thought of a number between 1 and 100!")

while True:
    try:
        g = input('Guess!')
        g = int(g)
        if not 100 > g > 0:
            print('It\'s in between 0 and 100!')
    except ValueError:
        print('Enter an integer')
        continue

    if g == n:
        print('Congratulations!')
        break

    if g < n:
        print('Larger')

    if g > n:
        print('Smaller')
