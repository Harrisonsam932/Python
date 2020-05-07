import os

path = 'e:/test/'
dircount = 0
filecount = 0
for item in os.listdir(path):
    p = path+item
    if os.path.isdir(p):
        dircount+=1
    else:
        filecount+=1
        
print(dircount)
print(filecount)
        