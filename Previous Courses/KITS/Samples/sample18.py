
print("""User must:
      * Start with PYT
      * Be more than 5 characters
      * Contain at least on '@'""")

user = input('Enter a User:')


pwd = input('Password:')

cpwd = input('Confirm Password:')

if len(user) >= 5 and user.count('@') > 0 and user.startswith('PYT') and pwd == cpwd:
    print('Registration success')
else:
    print('Registration Failed')
