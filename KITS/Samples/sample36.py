
dic1 = {101:'surya',102:'satya',103:'madhu',104:'maghana',105:'kiran',106:'rahul'}

dic2 = {101:'HYD',102:'CHN',103:'HYD',104:'BAN',105:'CHN',106:'HYD'}

city = input('Enter a city :')
flag = False
li = []
for item in list(dic2.values()):
    if item not in li:
        li.append(item)

if city not in li:
    print('No record found')
else:
    for item in list(dic2.keys()):
        if dic2[item] == city:
            print(item,'---',dic1[item],'---',dic2[item])
        
        




