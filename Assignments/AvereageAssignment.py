average1 = int(input("What is first mark? "))

average2 = int(input("What is second mark? "))

average3 = int(input("What is third mark? "))

totalaverage = ((average1 + average2 + average3)/3)

print(" ")
if totalaverage >= 60.0 and totalaverage <= 100:
    print("First Class!")

if totalaverage <= 30.0 and totalaverage < 60.0:
    print("Second Class.")

if totalaverage > 0 and totalaverage < 30.0:
    print("Third Class.")

print('Your average mark is:', (totalaverage), '%')
