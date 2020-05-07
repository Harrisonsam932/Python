import pymysql

conn = pymysql.Connect(host='localhost',port=3306,user='root',password='sutapalli',db='meghana')        

cur = conn.cursor()      
cur.execute("create table bank(accid int(4),accname varchar(20),accbal int(5))")
conn.commit()
cur.close()
conn.close()

                         