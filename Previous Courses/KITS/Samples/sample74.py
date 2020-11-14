import threading
import time

def displayTable():
    n = 9
    for i in range(1,11):
        print(n,'*',i,'=',n*i,'--->',threading.currentThread().getName())
        time.sleep(2)
        
t1 = threading.Thread(target=displayTable)
t1.setName('meghana')


t2 = threading.Thread(target=displayTable)
t2.setName('surya')

t3 = threading.Thread(target=displayTable)
t3.setName('satya')

t1.start()
t2.start()
t2.join()
t3.start()