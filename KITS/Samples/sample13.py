

name = 'MEGhana'  

print(name[0])

print(name[1:5])

print(name[3:])

print(name[:5])

print(len(name))

l = len(name)-1
while l>=0:
    print(name[l], end=' ')
    l -= 1

print(name[-1])

print(name[-4:-1])

for ch in reversed(name):
    print(ch)
