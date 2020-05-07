# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 14:15:22 2018

@author: nelson
"""

def reverse(li):
    for word in li:
        for rev_word in reversed(word):
            if rev_word.isalpha():
                print(rev_word, end="")
            else:
                print()
                break

fruits = ['ap!ple','bana@na','ma%ngo','#orange','pine*apple']
reverse(fruits)