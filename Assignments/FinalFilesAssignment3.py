# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:26:21 2018

@author: Harrison
"""

import os

path = input("Path: ")
count1 = 0
count2 = 0

if os.path.exists(path):
    for item in os.listdir(path):
        s = path + item
        if os.path.isfile(s):
            print(item)
            count1 += 1
        if os.path.isdir(s):
            print(item)
            count2 += 1
    print("There are", count1, "files and", count2, "folder(s)")
else:
    "Print no path found..."
