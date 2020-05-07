import threading
import time

def displayTable():
    n = 9
    for i in range(1,11):
        print(n,'*',i,'=',n*i,'--->',threading.currentThread().getName())
        time.sleep(1)
        
t1 = threading.Thread(target=displayTable)

print(t1.getName())
t1.setName('meghana')
print(t1.getName())
print(t1.isAlive())
t1.start()
print(t1.isAlive())



        

