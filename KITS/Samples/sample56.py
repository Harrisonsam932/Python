import os
opt = 'yes'

p = (input('enter a path:'))

if os.path.exists(p):
    if os.path.isfile(p):
        file1 = open(p,'a')
        while opt == 'yes':
            inp = (input('text please:'))
            if inp.startswith('su'):
                file1.write(inp)
                file1.write('\n')
            opt = (input('Do u want to continue:'))
        file1.close()   
    else:
        print('file not found')
