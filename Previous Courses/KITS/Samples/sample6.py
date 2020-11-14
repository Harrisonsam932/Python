

current_balance = (int)(input('Current Balance:'))
withdrawl = (int)(input('Withdrawl:'))

if withdrawl > current_balance:
    print('Insufficient Funds')
else:
    current_balance = current_balance-withdrawl
    print(current_balance)
