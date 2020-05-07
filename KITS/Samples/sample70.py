
class A:
    
    def display(self):
        for i in range(1,11):
            print(i)     
    
class B:
    
    def display(self):
        i = 10
        while i>=1:
            print(i)
            i-=1   
            
class C(B,A):
    
    def deleteKeyValue(self,key):
        dic = {101:'surya',102:'satya'}
        if key in dic:
            dic.pop(key)
            print(dic)
        else:
            print('Key not found')
            
obj = C()
obj.display()
obj.deleteKeyValue(111)



