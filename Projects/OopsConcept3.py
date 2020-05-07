 # -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 20:45:51 2018

@author: nelson
"""

#Static Method
class Even:
    x = 101
    
    @ staticmethod
    def FindEven():
        for i in range(1,101):
            if i%2 == 0:
                print(i)
            
    def FindOdd(self):
        for self.i in range(1,self.x):
            if self.i%2 != 0:
                print(self.i)
    
    def Display(self):
        self.FindOdd()
        print()
        self.FindEven()
                
obj = Even()
obj.Display()