

class SampleDemo:
    
    def display(self,*var):
        s = 0
        for item in var:
            s+=item
        print(s)
            
        
        
obj = SampleDemo()
obj.display(10,20,30,40,50)