# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 20:25:53 2018

@author: Harrison
"""

import threading
import time

def display():
    for i in range(1,11):
        print (i), '----', threading.current_thread().getName()
        time.sleep(1)
        
t1 = threading.Thread(target=display, name='surya')
t2 = threading.Thread(target=display, name='harrison')
t1.start()
t2.start()