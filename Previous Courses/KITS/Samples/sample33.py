
dic = {104:'meghana',102:'kiran',105:'rutvik',103:'surya',101:'raj'}

print(dic)

print(108 in dic)

print(dic.get(104))

print(list(dic.keys()))

print(list(dic.values()))

for item in dic.keys():
    print(item)

for item in dic.values():
    print(item)

for item in dic.items():
    print(item)

dic.popitem()
print(dic)

dic.pop(102)
print(dic)

dic.clear()

print(dic)

