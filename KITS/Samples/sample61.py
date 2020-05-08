class Car:

    steering = 1

    def moveleft(self):
        print('Car can move left using 1 steering')


li = []
for i in range(1, 16):
    li.append(Car())

for obj in li:
    obj.moveleft()
