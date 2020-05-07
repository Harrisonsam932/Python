class A:
    
    def __init__(self):
        self.x=1
        self.y=11
    
    def display1(self):
        for i in range(self.x,self.y):
            print(i)     
    
class B(A):
    
    def __init__(self):
        A.__init__(self)
        self.i=10
    
    def display2(self):
        while self.i>=1:
            print(self.i)
            self.i-=1 
            
obj = B()
obj.display1()
obj.display2()