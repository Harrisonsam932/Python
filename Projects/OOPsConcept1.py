# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 22:12:04 2018

@author: nelson
"""

name = input("What is your name? ")
class Vowel:
    vowelcount = 0
    start = 0
    end = len(name)
    
    def CountVowel(self):
        for c in name:
            if c in ('a','e','i','o','u','A','E','I','O','U'):
                   self.vowelcount += 1
            self.start += 1
        print(self.vowelcount)
        
class Case:
    casecount = 0
    start = 0
    end = len(name)
    
    def CaseCount(self):
        while self.start < self.end:
            if ord(name[self.start]) >= 65 and ord(name[self.start]) <= 90:
                self.casecount += 1
            self.start += 1
        print(self.casecount)


word1 = Vowel()
word2 = Case()
word1.CountVowel()
word2.CaseCount()