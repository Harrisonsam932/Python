
tup = (12,4.5,'surya',True,89,12)

print(len(tup))

print(tup[0])

print(tup[-1])

print(tup[2:5])

print(tup.count(12))

print(tup.index('surya'))

tup += (100,)

print(tup)

for item in tup:
    if type(item) == int:
        print(item)
        
for i in range(0,len(tup)):
    print(tup[i])
    
del(tup)
