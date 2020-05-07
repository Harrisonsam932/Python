
import os

def readFile(path):
    if os.path.exists(path):
        file1 = open(path,'r')
        for item in file1.readlines():
            print(item)
        file1.close()
    
    
    
p = 'e:/test/samplecopy.txt'    
readFile(p)