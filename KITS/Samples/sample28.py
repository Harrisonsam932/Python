user = (input('enter a username:'))
pwd = (input('password:'))
cpwd = (input('confirm password:'))

if len(user)>=5 and user.count('@')>0 and user.startswith('PYT') and pwd == cpwd:
    for ch in user:
        if ch.isdigit():
            print('registration success')
            break
else:
    print('registration failed')
