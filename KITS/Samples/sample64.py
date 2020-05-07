
class SampleDemo:
    
    def __init__(self):
        self.m=100
        self.n=200
        
    def displayEven(self):
        for i in range(self.m,self.n):
            if i%2 == 0:
                print(i)
        
obj = SampleDemo()    
obj.displayEven() 

