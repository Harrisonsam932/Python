

try:
    li = [1,2,3,4,5]
    print(li[0]+li[13])
except IndexError:
    print('Index not found in a List')