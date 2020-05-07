# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 11:12:20 2018

@author: nelson
"""

def reverse():
    string = input("Please enter text: ")
    for c in string[::-1]:
        print(c, end = '')
        
reverse()
        