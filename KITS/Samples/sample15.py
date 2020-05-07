
name = input("enter the word in question;")

rev = ''

for ch in reversed(name):
    rev += ch

if name == rev:
    print('Palindrome')
else:
    print('Not Palindrome')
