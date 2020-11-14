
import math

dic = {101: [67, 78, 77], 102: [56, 54, 46], 103: [32, 49, 23]}

for key in dic.keys():
    print(key, '---->', end=' ')
    tot = 0
    for item in dic[key]:
        tot += item
    print(tot)
    print()
