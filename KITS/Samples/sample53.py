
import os

path = 'e:/test/samplecopy.txt'
if os.path.exists(path):
    file1 = open(path,'r')
    print(file1.read())
    file1.close()