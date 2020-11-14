
import pymysql

conn = pymysql.Connect(host='localhost',port=3306,user='root',password='sutapalli',db='meghana')        
cur = conn.cursor()   

aid = (int)(input('Account Number:'))
aname = input('Account Name:')
abal = (int)(input('Account Balance:'))
   
cur.execute("insert into bank values(%d,'%s',%d)" % (aid,aname,abal))
conn.commit()
cur.close()
conn.close()

                         