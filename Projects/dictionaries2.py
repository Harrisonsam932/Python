# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:20:43 2018

@author: nelson
"""

dic1 = {101: [78,87,67], 102: [45,56,52], 103: [45,32,23]}

list1 = []
list2 = []
list3 = []

avg1 = []
avg2 = []
avg3 = []

for each in dic1[101]:
    list1.append(each)
    avg1.append(each)

avg1 = sum(list1) / len(list1)
print("101", "your total mark is:", sum(list1))
print("101", "your average is:", avg1)
print("")

for each in dic1[102]:
    list2.append(each)
    avg2.append(each)

avg2 = sum(list2) / len(list2)
print("102", "your total mark is:", sum(list2))
print("102", "your average is:", avg2)
print("")

for each in dic1[103]:
    list3.append(each)
    avg3.append(each)
    
print("103", "your total mark is:", sum(list3))
avg3 = sum(list3) / len(list3)
print("103", "your average is:", avg3)

print("")


    
    
    