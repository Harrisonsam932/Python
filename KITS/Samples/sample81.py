import pymysql

conn = pymysql.Connect(host='localhost',port=3306,user='root',password='sutapalli',db='meghana')        

cur = conn.cursor()      
cur.execute("insert into bank values(102,'meghana',2500)")
conn.commit()
cur.close()
conn.close()

                         