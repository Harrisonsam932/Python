
class SampleDemo:
    
    def __init__(self,p,q):
        self.m=p
        self.n=q
        
    def displayEven(self):
        for i in range(self.m,self.n):
            if i%2 == 0:
                print(i)
        
obj = SampleDemo(100,200)    
obj.displayEven() 

