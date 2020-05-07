num = []
name = []
m1 = []
m2 = []
m3 = []

start = 0
end = 5
#

while start < end:
    num.append(input("What is your student number? "))
    name.append(input("What is your name? "))
    m1.append(int(input("What is mark 1? ")))
    m2.append(int(input("What is mark 2? ")))
    m3.append(int(input("What is mark 3? ")))
    print("")
    start += 1

avg = []
avg.append(((m1[0]+m2[0]+m3[0])/3))
avg.append(((m1[1]+m2[1]+m3[1])/3))
avg.append(((m1[2]+m2[2]+m3[2])/3))
avg.append(((m1[3]+m2[3]+m3[3])/3))
avg.append(((m1[4]+m2[4]+m3[4])/3))

index = 0
for each in avg:
    if each > 60 and each <= 100:
        print("Class A")
    if each > 50 and each <= 60:
        print("Class B")
    if each > 35 and each <= 50:
        print("Class C")
    if each <= 35:
        print("Fail")
    index += 1

total = []
total.append(((m1[0]+m2[0]+m3[0])))
total.append(((m1[1]+m2[1]+m3[1])))
total.append(((m1[2]+m2[2]+m3[2])))
total.append(((m1[3]+m2[3]+m3[3])))
total.append(((m1[4]+m2[4]+m3[4])))

for each in total:
    print("Your total mark is:", each)

print("what is your name, Sir Alfred?")
