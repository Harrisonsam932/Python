
li = ['surya','surya','satya','Meghana','surya','kiran']
tup = ()
for item in li:
    if item == 'surya':
        tup += (item,)

for item in tup:
    li.remove(item)
    
print(li)
        
        