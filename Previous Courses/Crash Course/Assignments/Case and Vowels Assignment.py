
name = input("What is your first name? ")

casecount = 0
vowelcount = 0

for c in name:
    if c.isupper():
        casecount+=1
    if c in ('a','e','i','o','u','A','E','I','O','U'):
        vowelcount+=1

print("There are",casecount,'upper case letters.')
print("There are",vowelcount,'vowels')