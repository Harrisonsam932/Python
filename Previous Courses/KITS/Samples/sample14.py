
name = 'harrison'
s = ''
for i in range(0, len(name)):
    if i % 2 == 0:
        s += (chr)(ord(name[i])-32)
    else:
        s += name[i]

print(s)

print(ord("d"))
print(chr(119))
