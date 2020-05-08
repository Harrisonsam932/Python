
import os

path = "'c:\\users\harrison\desktop\python'"
if os.path.exists(path):
    file1 = open(path, 'r')
    print(file1.read())
    file1.close()
