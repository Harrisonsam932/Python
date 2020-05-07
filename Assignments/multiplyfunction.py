# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 11:10:48 2018

@author: nelson
"""

def multiply():
    start = 4
    end = 12

    while start <= end:
        n1 = 1
        stop = 12
        while n1 <= stop:
            print(start, '*', n1, '=', start*n1)
            n1+=1
            start+=1
            
multiply()