num = float(input('ENTER A NUMBER: '))

if num > 0:
    print(f'THE ABSOLUTE VALUE OF {num} is {num}')
elif num < 0:
    new_num = num*(-1)
    print(f'THE ABSOLUTE VALUE OF {num} is {new_num}')
else:
    print(f'0 IS NEUTRAL')
