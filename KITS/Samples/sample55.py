import os
path = "c:\\users\\harrison\\desktop\\test os\\text.txt"

print(os.path.exists(path))


txt = input('Enter a Text:')

file1 = open(path, 'a')

file1.write(txt)
file1.write('\n')

file1.close()
