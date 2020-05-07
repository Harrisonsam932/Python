import sample85

cur = sample85.Connection.getConnection()

aid = (int)(input('Account Number:'))
aname = input('Account Name:')
abal = (int)(input('Account Balance:'))
   
cur.execute("insert into bank values(%d,'%s',%d)" % (aid,aname,abal))
cur.connection.commit()
cur.close()


                         


