
value = input("Type in value: ")
tup = ()

con = ''

con = input('Do you want to start? ')

while con == 'y':
    if type(value) == int:
        print(tup)
        tup += (value,)
        print(tup)
        con = input("Do you want to continue? ")
        
    

print(tup)