import sample90
import sample91


bankObj = sample90.Bank()
dao = sample91.BankDAO()

bankObj.setaccid(111)
bankObj.setaccname('RAJU')
bankObj.setaccbal(9999)

dao.insertRecord(bankObj)

