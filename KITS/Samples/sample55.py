
path = 'e:/test/sample.txt'

txt = input('Enter a Text:')

file1 = open(path,'a')

file1.write(txt)
file1.write('\n')

file1.close()
