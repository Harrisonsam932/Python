

try:
    tup = (1,2,3)
    print(tup)
    del(tup)
    print(tup)
except NameError:
    print('Tuple already deleted')