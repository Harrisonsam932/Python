# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 23:16:43 2018

@author: nelson
"""

tup1 = (10, 20, 30, 10, 10, 40, 50, 20, 50, 50)
tup1reverse = ()

for each in tup1:
    count = tup1.count(each)
    if count > 1:
        tup1reverse += (each,)
        
count = 0
print(tup1reverse)

for num in tup1reverse:
    count = tup1reverse.count(num)
    if count > 1:
        tup1reverse.remove(num)
        
print(tup1reverse)