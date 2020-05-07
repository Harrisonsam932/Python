
class A:
    
    def countVowel(self,name):
        c = 0
        for ch in name:
            if ch in ('a','e','i','o','u'):
                c+=1
        return c    
    
class B:
    
    def displayReverse(self,name):
        for ch in reversed(name):
            print(ch)
            
class C(A,B):
    
    def deleteKeyValue(self,key):
        dic = {101:'surya',102:'satya'}
        if key in dic:
            dic.pop(key)
            print(dic)
        else:
            print('Key not found')
            

obj = C()
print(obj.countVowel('surya'))
obj.deleteKeyValue(102)
