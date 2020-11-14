

n = 23497239487234

while n > 0:
    rem = n % 10
    if rem % 2 == 0:
        print(rem, end=' ')
    n = n/10
