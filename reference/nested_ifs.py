print('HI THERE!')
num1 = float(input('PLEASE ENTER THE FIRST NUMBER: '))
num2 = float(input('PLEASE ENTER THE SECOND NUMBER: '))
num3 = float(input('PLEASE ENTER THE THIRD NUMBER: '))

#METHOD1
'''
if (num1>=num2) and (num1>=num3):
    print(f'{num1} is the greatest of all three numbers')
elif (num2>=num1) and (num2>=num3):
    print(f'{num2} is the greatest of all three numbers')
else:
    print(f'{num3} is the greatest of all three numbers')
'''

#METHOD2
if num1>num2:
    if num1>num3:
        print(f'{num1} is the greatest of all three numbers')
    else:
        print(f'{num3} is the greatest of all three numbers')
elif num2>num3:
    print(f'{num2} is the greatest of all three numbers')
else:
    print(f'{num3} is the greatest of all three numbers')
