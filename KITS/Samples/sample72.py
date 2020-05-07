class A:
    
    def display(self):
        for i in range(1,11):
            print(i)     
    
class B(A):
    
    def display(self):
        self.i=10
        while self.i>=1:
            print(self.i)
            self.i-=1 
            
obj = B()
obj.display()