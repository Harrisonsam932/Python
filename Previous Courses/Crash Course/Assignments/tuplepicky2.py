
con = 'yes'

tup = ()
tup.index()

while con == 'yes':
    value = input("Enter value: ")
    if value.isalpha():
        tup += (value,)

    con = input("do you want to continue: ")

print(tup)
