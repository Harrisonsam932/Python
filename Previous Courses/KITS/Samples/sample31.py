
# palindrome checker in a list.

li = ['surya', 'liril', 'satya']

for item in li:
    rev = ''
    for ch in reversed(item):
        rev += ch
    if item == rev:
        print(item)
