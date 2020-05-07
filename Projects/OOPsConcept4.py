# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:51:31 2018

@author: nelson
"""

class Text:
    def GetText(self,li):
        for item in li:
            print (item)
        
        
#class Numbers(Text):
    
    

#class Letters(Text):
    
    
obj = Text()
obj.GetText(['harry','surya','kiran'])