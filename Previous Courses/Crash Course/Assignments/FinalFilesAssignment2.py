# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:20:30 2018

@author: Harrison
"""

import os

userpath = input("Path: ")

path, dirs, files = next(os.walk(userpath))
file_count = len(files)

print(file_count)

