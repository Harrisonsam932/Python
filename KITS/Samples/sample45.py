

try:
    dic = {101: 'surya', 102: 'satya'}
    dic.pop(101)
    print(dic)
    li = [1, 2, 3, 4, 5]
    print(li[0]+li[3])
    name = None
    print(len(name))

except KeyError:
    print('Key not found to delete in dictionary')
except IndexError:
    print('Index not found in a List')
except SyntaxError:
    print("Something is wrong...")
except Exception as e:
    print(e)

finally:
    print('Welcome to Harrison')
