import sample85

class BankDAO:
    
    def __init__(self):
        self.cur = sample85.Connection.getConnection()
    
    
    def insertRecord(self,bankObj):
        self.cur.execute("insert into bank values(%d,'%s',%d)" % (bankObj.getaccid(),bankObj.getaccname(),bankObj.getaccbal()))
        self.cur.connection.commit()
        print('Record Inserted')
