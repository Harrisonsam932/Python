# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:01:00 2018

@author: nelson
"""

dic1 = {101: 'surya', 102: 'satya', 103: 'kiran', 104: 'pavan', 105: 'krishna'}

dic2 = {101: 'chennai', 102: 'delhi', 103: 'goa', 104: 'chennai', 105: 'delhi'}

city = input("Enter a City: ")

for each in dic2:
  if city == dic2[each]:
    print (each, '---', dic1[each])

if city in dic2:
    print("")
else:
  print("There are no records of students in this city.")