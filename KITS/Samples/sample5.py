
print("")
print("""This program will output your average grade
      over your classes. """)
total_classes = int(input("How many classes do you have: "))
a = []
final = 0
start = 0
while start < total_classes:
    b = int(input("Enter grade: "))
    a.append(b)
    start += 1


def average(final):
    final = sum(a)
    final /= total_classes
    print(final)


decision = input("Are you ready to see your average grade: ")
if decision == 'yes':
    average(final)

else:
    print("n00b")

'''

m1 = int(input('Enter a Value:'))
m2 = int(input('Enter a Value:'))
m3 = int(input('Enter a Value:'))

print('Total:', m1+m2+m3)
avg = (m1+m2+m3)/3
print('Average:', (m1+m2+m3)/3)

if avg >= 60:
    print('First Class')
elif avg >= 50 and avg < 60:
    print('Second Class')
elif avg >= 35 and avg < 50:
    print('Third Class')
else:
    print('Failed')
'''
