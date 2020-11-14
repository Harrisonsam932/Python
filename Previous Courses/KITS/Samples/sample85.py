
import pymysql

class Connection:
    
    @ staticmethod
    def getConnection():
        conn = pymysql.Connect(host='localhost',port=3306,user='root',password='sutapalli',db='meghana')        
        cur = conn.cursor()   
        return cur

