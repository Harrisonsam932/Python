

try:
    n = (int)(input('Enter a Number:'))
    print(n*n)
except ValueError:
    print('String cannot be convert into Integer')