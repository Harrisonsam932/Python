# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymysql

conn = pymysql.Connect(host='localhost',port=3306,user='root',password='Harrison32458',db='mypython')

cur = conn.cursor()

cur.execute("insert into student values(101,'Harrison', 'Thunder Bay'")
cur.execute("insert into student values(102, 'Jeremy', 'Thunder Bay'")
cur.execute("insert into student values(103, 'Surya', 'Chennai'")

conn.commit()