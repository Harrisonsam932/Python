import sample85

cur = sample85.Connection.getConnection()

cur.execute('delete from bank where accid=104')

cur.connection.commit()
cur.close()