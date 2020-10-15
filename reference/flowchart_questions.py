#SIMPLE INTEREST
'''
print('HI THERE!')
p = float(input('PLEASE ENTER THE PRINCIPAL AMOUNT: '))
r = float(input('PLEASE ENTER THE RATE OF INTEREST: '))
t = float(input('PLEASE ENTER THE TIME PERIOD: '))

simple_interest = (p*r*t)/100
print(f'THE SIMPLE INTEREST IS {simple_interest}')
'''

#PRINT TOTAL AMOUNT TO BE PAID AS PER CRITERIA: A)FIRST 5 HOURS -10QR/H 2)NEXT 5 HOURS - 15QR/H  3)ABOVE 10HRS - 20QR/H
#AND RENTAL CHARGE IS 100QR
'''
print('HI THERE!')
hours = float(input('PLEASE ENTER THE NUMBER OF HOURS: '))

if hours < 1:
    print('PLEASE ENTER A NUMBER GREATER THAN 0.')
elif (hours>=1) and (hours<=5):
    total_1 = 100 + hours*10
    print(f'THE TOTAL AMOUNT, INCLUDING THE RENTAL CHARGE, TO BE PAID IS: {total_1}')
elif (hours>=6)and(hours<=10):
    h_new = hours-5
    total_2 = 100 + 50 + h_new*15
    print(f'THE TOTAL AMOUNT, INCLUDING THE RENTAL CHARGE, TO BE PAID IS: {total_2}')
else:
    h_last = hours-10
    total_3 = 100 + 50 + 75 + h_last*20
    print(f'THE TOTAL AMOUNT, INCLUDING THE RENTAL CHARGE, TO BE PAID IS: {total_3}')
'''
'''
print('HI THERE!')
hours = float(input('PLEASE ENTER THE NUMBER OF HOURS: '))

if hours < 1:
    print('PLEASE ENTER A NUMBER GREATER THAN 0.')
elif (hours>=1) and (hours<=5):
    total_1 = 100 + hours*10
    print('THE TOTAL AMOUNT, INCLUDING THE RENTAL CHARGE, TO BE PAID IS:', total_1)
elif (hours>=6)and(hours<=10):
    h_new = hours-5
    total_2 = 100 + 50 + h_new*15
    print('THE TOTAL AMOUNT, INCLUDING THE RENTAL CHARGE, TO BE PAID IS:', total_2)
else:
    h_last = hours-10
    total_3 = 100 + 50 + 75 + h_last*20
    print('THE TOTAL AMOUNT, INCLUDING THE RENTAL CHARGE, TO BE PAID IS:', total_3)
''' 
#PRINT PALIDROME
print('HI THERE!')
num = int(input('PLEASE ENTER THE NUMBER: '))
store = 0

while num >= 0:
    r = num%10
    store = (store*10)+r
    num = num//10
    
if store == num:
    print(f'THE NUMBER {num} IS PALINDROME {store}')
else:
    print('THE NUMBER IS NOT A PALINDROME')



#PRINT THE PRODUCT OF TWO NUMBERS
'''
print('HI THERE!')
num1 = float(input('PLEASE ENTER THE FIRST NUMBER: '))
num2 = float(input('PLEASE ENTER THE SECOND NUMBER: '))

prod = num1*num2

print(f'THE PRODUCT THE TWO NUMBERS IS {prod}')
'''

#PRINT N NATURAL NUMBERS
#INPUT A NUMBER AND FIND WHETER ITS PRIME OR NOT
#SUM AND AVERAGE OF FIRST N NATURAL NUMBERS
#INPUT RADIUS AND FIND AREA AND PERIMETER OF CIRCLE
#INPUT 3 ANGLES AND FIND WHAT KIND OF TRIANGLE
#INPUT A NUMBER AND FIND FACTORIAL
