# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:56:26 2018

@author: nelson
"""


def checkname():
    choice = 'yes'    
    dic = {}
    n = 101
    while choice == 'yes':
        name = input("Enter a name: ")
        if name.startswith('su') and name.isalpha():
            dic[n]=name
        n+=1
        choice = input("Do you want to continue? ")
    print(dic)
        
checkname()