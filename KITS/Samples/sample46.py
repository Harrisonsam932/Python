
def display():
    for i in range(1,11):
        print(i)
    

def table():
    n = 9
    for i in range(1,11):
        print(n,'*',i,'=',(n*i))
        
def countUpper(name):
    count = 0
    for ch in name:
        if ch.isupper():
            count+=1
    print(count)
    
def findDuplicates(li):
    tup = ()
    for item in li:
        if li.count(item)>1 and item not in tup:
            tup += (item,)
    print(tup)
    

def reverse(str1):
    for ch in reversed(str1):
        print(ch, end=' ')
        
def sumNatural():
    s = 0
    for i in range(10,26):
        s += i
    return s

def getValues():
    tup = ('surya','meghana','srikanth','satya','suresh')
    li = [] 
    for item in tup:
        if item.startswith('su'):
            li.append(item)
    return li

def validatePalindrome(name):
    rev = ''
    for ch in reversed(name):
        rev += ch
    if name == rev:
        return True
    else:
        return False
    


        
        

        
        

        
    