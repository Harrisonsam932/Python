
name = 'welcome to python'

start = 0
length = len(name)

while start < length:
    if start%2 == 0:
        print(name[start].upper(), end="")
    else:
        print(name[start], end="")
    start+=1