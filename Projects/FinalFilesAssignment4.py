# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:26:21 2018

@author: Harrison
"""

import os

path = input("Path: ")
print("""Option 1 - files
Option 2 - folders""")
option = input("What option would you like: ")
ext = input("What type of extension would you like: ")
opt = 'y'

def Files():
    if os.path.exists(path) == True:
        for item in os.listdir(path):
            if item.endswith('.'+ext):
                print(item)

    else:
        print("There is no such path")

def Folders():
    if os.path.exists(path) == True:
        for item in os.listdir(path):
            s = path + item
            if os.path.isdir(s):
                print(item)
    else:
        print("There is no such path")
        
if option == 1:
    Files()
else:
    Folders()
        
#for item in os.listdir(path):
 #   s = path + item
  #  if os.path.isfile(s):
   #     print(item)
    #    count1 += 1
    #if os.path.isdir(s):
     #   print(item)
      #  count2 += 1
#print("There are", count1, "files and", count2, "folder(s)")