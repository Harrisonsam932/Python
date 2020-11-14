
import sample85

cur = sample85.Connection.getConnection()
cur.execute("select count(*) from bank")
tup = cur.fetchone()
print('No of Records=',tup[0])