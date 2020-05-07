
import os

print(os.getcwd())

print(os.getpid())

#print os.mkdir('e:/test/meghana')

for i in os.listdir('e:/meghana'):
    print(i)
    
for i in os.walk('e:/meghana'):
    print(i)
    
print(os.path.exists('e:/meghana'))
print(os.path.isdir('e:/meghana'))
print(os.path.isfile('e:/meghana'))
    
