
import pymysql

conn = pymysql.Connect(host='localhost',port=3306,user='root',password='sutapalli',db='meghana')        

cur = conn.cursor()      
cur.execute("Hai")
conn.commit()
cur.close()
conn.close()

                         