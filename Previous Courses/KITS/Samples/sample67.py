
class Father:
    fproperty = 10
    
class Son(Father):
    sproperty = 5
    
    
s = Son()
print(s.sproperty+s.fproperty)