import pymysql
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', user='root', password='Harrison32458', database='testdb'
)

conn = pymysql.Connect(host='localhost', port=3306,
                       user='root', password='Harrison32458')


mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)


cur = conn.cursor()
cur.execute("insert into bank values(102,'harrison',2500)")
conn.commit()
cur.close()
conn.close()
'''
