ch = input("Enter a letter to check if it's a vowel or not: ")

if ch in ('a', 'e', 'i', 'o', 'u') or ch.upper() in ('A', 'E', 'I', 'O', 'U'):
    print('vowel')
else:
    print('not vowel')
