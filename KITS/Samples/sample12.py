# This first part gives the number's multiples...

for i in range(1, 15):
    if i % 5 == 0:
        print(i)

n = 9
for i in range(1, 11):
    print(n, '*', i, '=', i*n)

# ASCII practice
name = 'harrison'
for ch in name:
    print((chr)(ord(ch)-32), end='')
