
tup = ('suryanarayana', 'welcome', 'meghana')

tup = ()
opt = 'yes'
while opt == 'yes':
    lol = input("Enter a string: ")
    tup += (lol,)
    opt = input("Do you want to continue?")

for item in tup:
    dup = ()
    for ch in item:
        if ch not in dup:
            dup += (ch,)
            count = item.count(ch)
            print(ch, '-->', end=' ')
            for i in range(0, count):
                print ('$', end=' ')
            print()
