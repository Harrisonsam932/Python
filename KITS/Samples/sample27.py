

str1 = 'satyanarayana'

str2 = 'surya'

str3 = ''

l1 = len(str1)
l2 = len(str2)

if l2 > l1:
    for i in range(0,l1):
        str3 += str1[i]+str2[i]
    str3 += str2[l1:]
else:
    for i in range(0,l2):
        str3 += str1[i]+str2[i]
    str3+= str1[l2:]
    
print(str3)
        
