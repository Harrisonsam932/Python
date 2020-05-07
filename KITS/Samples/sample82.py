
import pymysql

conn = pymysql.Connect(host='localhost',port=3306,user='root',password='sutapalli',db='meghana')        

cur = conn.cursor()      
cur.execute("update bank set accbal=accbal+2500 where accid = 102")
conn.commit()
cur.close()
conn.close()

                         