
tup = ()

opt = 'yes'

while opt == 'yes':
    str1 = input('Enter a String:')
    if not str1.isalpha():
        count = 0
        tup += (str1,)
        for ch in str1:
            if ch in ('!', '@', '#', '$', '%', '^', '&', '*'):
                count += 1
        print(str1, ' contains ', count, ' special characters')

    opt = input('Do u want to continue:')

