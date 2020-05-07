
import threading
import time

class ThreadDemo(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        n = 9
        for i in range(1,11):
            print(n,'*',i,'=',n*i,'--->',threading.currentThread().getName())
            time.sleep(2)


t1 = ThreadDemo()
t1.setName('meghana')

t2 = ThreadDemo()
t2.setName('surya')

t3 = ThreadDemo()
t3.setName('satya')

t1.start()
t1.join()
t2.start()
t3.start()
        
        
    
    
        
    
    