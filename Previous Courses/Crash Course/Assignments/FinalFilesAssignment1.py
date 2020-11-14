# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:43:37 2018

@author: Harrison
"""

import os

print (os.getcwd())

os.mkdir('c:/users/Harrison/FinalFilesAssignment/')

os.chdir('c:/users/Harrison/FinalFilesAssignment')

print(os.getcwd())

path = input("Enter a path: ")
filecount = 0
dircount = 0
files = (os.listdir(path))
def valid_path(dir_path, filename):
    full_path = os.path.join(dir_path, filename)
    return os.path.isfile(full_path)
