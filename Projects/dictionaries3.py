# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:11:48 2018

@author: nelson
"""

dict = {101: 'sur&ya', 102: 'kir!an', 103: 'krishna(', 104: 'pavan', 105: '@satya'}

list = ('')
final = ("")

for each in dict.get(101):
    list+=(each)

for c in list[::-1]:
    if c.isalpha():
        final+=(c)
        
    else:
        break

print('101', '----->',final)
