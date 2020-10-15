#PROGRAM1 ---> PRINT WELCOME MSG
'''
print('HI THERE!')
name = str(input('PLEASE ENTER YOUR NAME: '))
wel = str(input('PLEASE ENTER A WELCOME MESSAGE: '))

print(f'HI {name}. YOUR WELCOME MESSAGE IS {wel}.')
'''

#PROGRAM2 ---> INPUT TWO NUMBERS AND PRINT THEIR SUM
'''
print('HI THERE!')
num1 = float(input('PLEASE ENTER THE FIRST NUMBER: '))
num2 = float(input('PLEASE ENTER THE SECOND NUMBER: '))
sum = num1+num2

#print('The sum og the numbers is\t',sum)
print(f'THE SUM OF THE NUMBERS IS {sum}')
'''

#PROGRAM3 ---> INPUT 'X' AND 'N' AND COMPUTE X POWER N
'''
print('HI THERE!')
x = int(input('PLEASE ENTER THE BASE NUMBER: '))
n = int(input('PLEASE ENTER THE EXPONENT NUMBER: '))
num = x**n

print(f'{x} raised to the power {n} is {num}')
'''

#PROGRAM4 ---> INPUT 2 NUMBERS AND FIND THE GREATEST NUMBER
'''
print('HI THERE!')
num1 = float(input('PLEASE ENTER THE FIRST NUMBER: '))
num2 = float(input('PLEASE ENTER THE SECOND NUMBER: '))

if num1 > num2:
    print(f'{num1} is the greater number.')
elif num1 == num2:
    print(f'Both the numbers are equal.')
else:
    print(f'{num2} is the greater number.')
'''

#PROGRAM4 ---> INPUT 3 NUMBERS AND FIND THE GREATEST NUMBER
'''
print('HI THERE!')
num1 = float(input('PLEASE ENTER THE FIRST NUMBER: '))
num2 = float(input('PLEASE ENTER THE SECOND NUMBER: '))
num3 = float(input('PLEASE ENTER THE THIRD NUMBER: '))

if (num1>=num2) and (num1>=num3):
    print(f'{num1} is the greatest of all three numbers')
elif (num2>=num1) and (num2>=num3):
    print(f'{num2} is the greatest of all three numbers')
else:
    print(f'{num3} is the greatest of all three numbers')


#elif (num3>num1) and (num3>num2):
    #print(f'{num3} is the greatest of all three numbers')
'''

#EXTRA_PROGRAM ---> INPUT 3 NUMBERS AND FIND THE SMALLEST NUMBER
'''
print('HI THERE!')
num1 = float(input('PLEASE ENTER THE FIRST NUMBER: '))
num2 = float(input('PLEASE ENTER THE SECOND NUMBER: '))
num3 = float(input('PLEASE ENTER THE THIRD NUMBER: '))

if (num1<=num2) and (num1<=num3):
    print(f'{num1} is the smallest of all three numbers')
elif (num2<=num1) and (num2<=num3):
    print(f'{num2} is the smallest of all three numbers')
else:
    print(f'{num3} is the smallest of all three numbers')
'''

#EXTRA_PROGRAM
'''
print('HI THERE!')
num = float(input('PLEASE ENTER YOUR MARK: '))

if (num>=0) and (num<61):
    print(f'{num} gives you grade F')
elif (num>=61) and (num<81):
    print(f'{num} gives you grade B')
else:
    print(f'{num} gives you grade A')
'''

#PROGRAM5 ---> INPUT 3 NUMBERS AND FIND THE SUM AND AVERAGE
'''
print('HI THERE!')
num1 = float(input('PLEASE ENTER THE FIRST NUMBER: '))
num2 = float(input('PLEASE ENTER THE SECOND NUMBER: '))
num3 = float(input('PLEASE ENTER THE THIRD NUMBER: '))

total = num1+num2+num3
avg = total/3

print(f'The sum of the three numbers is {total} and their average is {avg}')
'''

#PROGRAM6 ---> INPUT TEMP AND CONVERT FROM F TO C OR VICE VERSA
'''
print('HI THERE!')
which_temp = input('WHAT FORM OF TEMPERATURE ARE YOU GOING TO ENTER? F OR C: ')

if which_temp == 'F':
    temp_f = float(input('ENTER TEMP IS FAHRENHEIT: '))
    celsius_1 = (temp_f - 32)*5
    celsius_2 = celsius_1 / 9
    print(f'The given temperature {temp_f} in celcius is {celsius_2}')

elif which_temp == 'C':
    temp_c = float(input('ENTER TEMP IS CELSIUS: '))
    fahrenheit = (temp_c*1.8)+32
    print(f'The given temperature {temp_c} in fahrenheit is {fahrenheit}')

else:
    print("ENTER ONLY 'F' OR 'C'")
'''

#PROGRAM7 ---> INPUT 2 NUMBERS AND INTERCHANGE OR SWAP
'''
print('HI THERE!')
num1 = str(input('PLEASE ENTER THE FIRST NUMBER: '))
num2 = float(input('PLEASE ENTER THE SECOND NUMBER: '))

###METHOD1
print(f'The old first number is {num1} and second number is {num2}')
num1,num2 = num2,num1
print(f'The new first number is {num1} and second number is {num2}')

###METHOD2
print(f'The old first number is {num1} and second number is {num2}')
temp_num = num1
num1 = num2
num2 = temp_num
print(f'The new first number is {num1} and second number is {num2}')

###METHOD3 (ONLY NUMERICAL VALUES)
print(f'The old first number is {num1} and second number is {num2}')
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print(f'The new first number is {num1} and second number is {num2}')
'''

#PROGRAM8 ---> INPUT A NUMBER AND FIND WHETHER ODD OR EVEN
'''
print('HI THERE!')
num = int(input('PLEASE ENTER THE NUMBER: '))
r = num%2

if num == 0:
    print('0 IS NEITHER ODD NOR EVEN')
elif r == 0:
    print(f'{num} is an EVEN number')
else:
    print(f'{num} is an ODD number')
'''

#PROGRAM9 ---> INPUT A NUMBER AND FIND WHETHER NEGATIVE OR POSITIVE
'''
print('HI THERE!')
num = float(input('PLEASE ENTER THE NUMBER: '))

if num < 0:
    print(f'{num} is NEGATIVE')
elif num > 0:
    print(f'{num} is POSITIVE')
else:
    print(f'{int(num)} is neither positive nor negative')
'''

#PROGRAM10 ----> MENU-DRIVEN PROGRAM TO FIND (1)AREA OF A TRIANGLE, (2)TO FIND AREA OF CIRCLE AND IF NO CHOICES ARE OPTED, FIND CIRCUMFERENCE OF CIRLE
'''
import constant
print('HI THERE!')
ques = int(input('WHAT DO YOU WANT TO FIND?\n1:AREA OF TRIANGLE, 2:AREA OF CIRCLE, ANY NUMBER:CIRCUMFERENCE\nENTER EITHER 1,2 or ANY OTHER NUMBER: '))
if ques == 1:
    b = float(input('ENTER THE BASE OF THE TRIANGLE: '))
    h = float(input('ENTER THE HEIGHT OF THE TRIANGLE: '))
    area_tri = 0.5*b*h
    print(f'{area_tri} sq.unit is the area of the triangle')
elif ques == 2:
    rad = float(input('ENTER THE RADIUS OF THE CIRCLE: '))
    area_cir = constant.pi*(rad**2)
    print(f'{area_cir} sq.unit is the area of the circle')
else:
    print("WE'LL FIND THE CIRCUMFERENCE OF A CIRCLE")
    r = float(input('ENTER THE RADIUS OF THE CIRCLE: '))
    cir = 2*constant.pi*r
    print(f'{cir} is the circumference of the circle')
'''

#CALCULATE SIMPLE AND COMPUND INTEREST
'''
print('HI THERE')
p = float(input('ENTER THE PRINCIPAL AMOUNT: '))
r = float(input('ENTER THE RATE OF INTEREST: '))
t = float(input('ENTER THE TIME PERIOD: '))

s_interest = (p*r*t)/100
print(f'THE SIMPLE INTEREST AT THE END OF {t} YEARS IS {s_interest}')

t_new = int(t)
for a in range(1,t_new):
    c_1 = 1+(r/100)
    c_2 = (c_1)**t
    c_interest = c_2*p
    p = c_interest

print(f'THE COMPOUND INTEREST AT THE END OF {t} YEARS IS {c_interest}')
'''

#SERIES
'''
rows = int(input('HOW MANY ROWS ARE REQUIRED: '))
count = 1
number = 1
for b in range(rows):
    for i in range(count):
        print(number, end=" ")
        number +=1
    print('')
    count += 1
    continue
'''

#FREQUENCY DISTRIBUTION TABLE OF THE PERCENTAGE MARKS IN COMP SCIENCE OF 10 STUDENTS
'''
print('HI THERE!')
n = int(input('HOW MNAY STUDENTS ARE INCLUDED: '))
fail = pas = good = v_good = skip = 0

for a in range(1,n+1):
    perc = float(input('PLEASE ENTER THE PERCENTAGE OBTAINED: '))
    if perc < 0:
        print('PLEASE ENTER A VALUE GREATER THAN OR EQUAL TO 0')
        skip += 1
        continue
    elif perc >= 0 and perc < 34:
        fail +=1
        continue
    elif perc >= 34 and perc < 60:
        pas +=1
        continue
    elif perc >= 60 and perc < 80:
        good +=1
        continue
    elif perc >= 80 and perc <= 100:
        v_good +=1
        continue
    else:
        print('PLEASE ENTER A VALUE BETWEEN 0 TO 100')
        skip += 1

if skip == 0:
    print(f'THEREFORE, OUT OF {n} STUDENTS\n{fail} - FAIL\n{pas} - PASS\n{good} - GOOD \n{v_good} - VERY GOOD')
else:
    print(f'THEREFORE, OUT OF {n} STUDENTS\n{fail} - FAIL\n{pas} - PASS\n{good} - GOOD \n{v_good} - VERY GOOD\n{skip} - SKIPPED')
'''

#PROGRAM TO COUNT THE NUMBER OF VOWELS PRESENT IN A STRING
'''
print('HI THERE!')
sentence = input('ENTER A STRING: ')
count = len(sentence)
vowels = ['a','e','i','o','u','A','E','I','O','U']
number = 0
consonants = 0

for a in range(count):
    check = sentence[a]
    if check in vowels:
        number += 1
    else:
        consonants += 1

print(f'IN THE GIVEN SENTENCE \'{sentence}\' THERE ARE\nVOWELS - {number}\nCONSONANTS - {consonants}')
'''
#PROGRAM





















