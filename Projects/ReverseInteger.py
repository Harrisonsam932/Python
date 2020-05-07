# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 20:28:21 2018

@author: harrison nelson
"""

Number = int(input("What number would you like to reverse?"))    
Reverse = 0    
while(Number > 0):    
    Remainder = Number %10    
    Reverse = (Reverse *10) + Remainder    
    Number = Number // 10    
     
print("\n Reverse of entered number is = " ,Reverse)