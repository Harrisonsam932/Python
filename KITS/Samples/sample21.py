
tup = (10, 23, 45, 32, 19, 29)

ecount = 0
ocount = 0

for each in tup:
    if each % 2 == 0:
        ecount += 1
    else:
        ocount += 1

print('Even Count:', ecount)
print('Odd Count:', ocount)
