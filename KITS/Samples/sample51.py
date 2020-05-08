
import os
print(os.getpid())

new = os.getcwd()

# # os.mkdir(new)

# print(os.mkdir(os.getcwd() + '\\test os-module'))

for i in os.listdir("c:\\users\harrison\desktop\python\kits"):
    print(i)

for i in os.walk("c:\\users\harrison\desktop\python\kits"):
    print(i)
'''
print(os.path.exists('\test os-module'))
print(os.path.isdir('\test os-module'))
print(os.path.isfile('\test os-module'))
'''

print(os.listdir("c:\\users\harrison\desktop\python\kits"))
print(os.path.isdir(new))

print(os.path.isfile(new))
