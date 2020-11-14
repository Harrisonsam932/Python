
name = input("What is your first name? ")

casecount = 0
vowelcount = 0

start=0
end = len(name)

while start < end:
    if ord(name[start])>=65 and ord(name[start])<=90:
        casecount+=1
    if name[start] in ('a','e','i','o','u','A','E','I','O','U'):
        vowelcount+=1
    start+=1    

print("There are",casecount,'upper case letters.')
print("There are",vowelcount,'vowels')