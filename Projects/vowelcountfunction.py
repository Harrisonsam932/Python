# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:36:50 2018

@author: nelson
"""

name = 'welcome to LLLLLpython'
count = 0
case = 0
    
def vowelcount():
   count = 0 
   for c in name:
       if c in ('a','e','i','o','u'):
           count +=1
   print(count)

def casecount():
    case = 0
    for c in name:
        if c.isupper():
            case +=1
    print(case)
    
vowelcount()
casecount()