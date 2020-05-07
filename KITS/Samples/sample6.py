

curr_bal = (int)(input('Current Balance:'))
with_drawl = (int)(input('Withdrawl:'))

if with_drawl > curr_bal:
    print('Insufficient Funds')
else:
    curr_bal = curr_bal-with_drawl;
    print(curr_bal)