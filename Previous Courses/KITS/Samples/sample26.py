

tup = ('sury@a','Saty!a','Kir&an')

sup = ()

for item in tup:
    str1 = ''
    for ch in item:
         if ch not in ('!','@','#','$','%','^','&','*'):
                       str1+=ch
    sup+=(str1,)
    
print(sup)
                       