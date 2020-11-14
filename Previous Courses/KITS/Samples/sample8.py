
# This is a program that creates multiplication tables.

start = 1
num = int(input("Enter a table:"))

while start <= 10:
    print(num, 'x', start, '=', num*start)
    start += 1
