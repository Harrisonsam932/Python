

m1 = (int)(input('Enter a Value:'))
m2 = (int)(input('Enter a Value:'))
m3 = (int)(input('Enter a Value:'))

print('Total:',m1+m2+m3)
avg = (m1+m2+m3)/3
print('Average:',(m1+m2+m3)/3)

if avg >=60:
    print('First Class')
elif avg >=50 and avg <60:
    print('Second Class')
elif avg >= 35 and avg < 50:
    print('Third Class')
else:
    print('Failed')