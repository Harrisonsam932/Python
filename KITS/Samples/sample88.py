
import sample85

cur = sample85.Connection.getConnection()
cur.execute("select * from bank where accname in ('surya','meghana')")

for item in cur.fetchall():
    print(item[0],'---',item[1],'---',item[2])
