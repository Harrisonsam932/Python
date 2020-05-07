
li = ['surya','meghana','kiran','srikanth']

name = input('Enter a Name:')

for item in li:
    if item[0:2] == name[0:2]:
        ind = li.index(item)+1
        break
li.insert(ind,name)
print(li)