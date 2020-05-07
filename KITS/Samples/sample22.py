
tup = ()

opt = 'yes'

while opt == 'yes':
    str1 = input('Enter a String:')
    if not str1.isalpha():
        tup += (str1,)
    
    opt = input('Do u want to continue:')

print(tup)
