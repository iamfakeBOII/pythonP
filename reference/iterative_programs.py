#INPUT A NUMBER AND FIND WHETHER IT IS PRIME OR NOT
'''
print('HI THERE!')
num = int(input('ENTER THE REQUIRED NUMBER/INTEGER: '))

if num<1:
    print('ENTER A NUMBER GREATER THAN 0')
elif num == 1:
    print('1 IS NEITHER PRIME NOR COMPOSITE')
elif num == 2:
    print('2 IS A PRIME NUMBER')
else:
    for i in range(2,num,1):
        check = num%i
        if check == 0:
            print(f'{num} IS COMPOSITE')
            break
    else:
        print(f'{num} IS PRIME')
'''

#PRINT THE FIBONACCI SERIES OF N NUMBERS
'''
print('HI THERE!')
num = int(input('ENTER THE NUMBER OF FIBONACCI NUMBERS REQUIRED: '))

if num<1:
    print('ENTER A NUMBER GREATER THAN 0')
elif num == 1:
    print('THE FIRST FIBONACCI NUMBER IS 0')
elif num == 2:
    print('THE FIRST TWO FIBONACCI NUMBERS ARE [0,1] ')
else:
    l = 0
    r = 1
    count = 2
    series  =[0,1]
    while count<num:
        sum = l+r
        series.append(sum)
        l = r
        r = sum
        count += 1

print(f'THE FIRST {num} FIBONACCI NUMBERS ARE {series} ')
'''

#FIND SUM OF N NATURAL NUMBER
'''
print('HI THERE!')
num = int(input('ENTER THE NUMBER OF NATURAL NUMBERS TO BE ADDED: '))

s = num*(num+1)
sum = s/2
print(f'THE SUM OF {num} natural numbers is {sum}')
'''

#PRINT N NATURAL NUMBERS
'''
print('HI THERE!')
num = int(input('ENTER THE NUMBER OF NATURAL NUMBERS REQUIRED: '))

if num<1:
    print('ENTER A VALUE GREATER THAN 0')
else:
    nat_nums = []
    for n in range(1,num+1):
        nat_nums.append(n)

print(f'THE FIRST {num} NATURAL NUMBERS ARE {nat_nums}')
'''

#EVEN NUMBERS FROM 1 TO N
'''
print('HI THERE!')
num = int(input('ENTER THE NUMBER OF EVEN NUMBERS REQUIRED: '))

for n in range(1,num+1):
    print(2*n)
'''

#FACTORIAL
'''
print('HI THERE!')
num = int(input('ENTER THE NUMBER WHOSE FACTORIAL IS REQUIRED: '))

if num<0:
    print('ENTER A VALUE GREATER THAN OR EQUAL TO 0')
elif num == 0:
    print('THE FACTORIAL OF 0 IS 1')
else:
    i = 1
    f = 1
    while i<=num:
        f = f*i
        i += 1

    print(f'THE FACTORIAL OF {num} is {f}')
'''

#PALINDROME
'''
print('HI THERE!')
num = int(input('PLEASE ENTER THE NUMBER: '))
n = num
store = 0

if num<1:
    print('ENTER A NUMBER GREATER THAN 0')
else:
    while num>0:
        last = num%10
        store = (store*10)+last
        num = num//10

if store == n:
    print('SINCE', store, 'IS THE REVERSE OF', n, 'THE NUMBER IS PALINDROME')
else:
    print('THE NUMBER IS NOT A PALINDROME')
'''

#PRINT SERIES X POWER N
'''
print('HI THERE!')
base = int(input('PLEASE ENTER THE BASE NUMBER: '))
power = int(input('PLEASE ENTER THE POWER: '))
nums = []

for a in range(0,power+1):
    final = base**a
    nums.append(final)

final_sum = sum(nums)
print(f'THE FINAL ANSWER OF THE SEQUENCE IS {final_sum}')
'''

#ARMSTRONG
'''
print('HI THERE!')
num = int(input('ENTER THE NUMBER WHICH HAS TO BE CHECKED: ')) #INITIALISATION OF NUM VARIABLE
check = num
power = len(str(num)) #TO FIND OUT THE NUMBER OF DIGITS
store = 0

if num<1:
    print('ENTER A NUMBER GREATER THAN 0')
else:
    while num>0: #CONDITIONS
        last = num%10 #OBTAIN LAST DIGIT
        store = store + (last**power)
        num = num//10 #UPDATION

    if store == check:
        print(f'SINCE THE OBTAINED NUMBER {store} IS EQUAL TO {check}, THE NUMBER IS AN ARMSTRONG NUMBER')
    else:
        print(f'ITS NOT AN ARMSTRONG NUMBER')
'''

#PERFECT NUMBER
'''
print('HI THERE!')
num = int(input('ENTER THE NUMBER WHICH HAS TO BE CHECKED: '))
check = num
store = 0
#factors = []

for b in range(1,num):
    if num%b == 0:
        store = store + b

#final = sum(factors)

if store == check:
    print(f'{check} = THE SUM OF FACTORS OF {store}.\n SO {check} IS A PERFECT NUMBER')
else:
    print(f'{check} IS NOT EQUAL TO THE SUM OF {store}.\n SO {check} IS NOT A PERFECT NUMBER')
'''

#GREATEST COMMON DIVISOR
'''
print('HI THERE!')
num1 = int(input('ENTER THE FIRST NUMBER REQUIRED: '))
num2 = int(input('ENTER THE SECOND NUMBER REQUIRED: '))
factors1 = [num1]
factors2 = [num2]

for b in range(1,num1):
    div = num1%b
    if div == 0:
        factors1.append(b)

for b in range(1,num2):
    div = num2%b
    if div == 0:
        factors2.append(b)

if num1<num2:
    check = max(factors1)
    if check in factors2:
        print(f'THE GREATEST COMMON DIVISOR IN {num1} AND {num2} IS {check}')
    else:
        print(f'THE TWO NUMBERS HAVE NO COMMON FACTORS. SO THE GREATEST COMMON DIVISOR IS 1')
else:
    check = max(factors2)
    if check in factors1:
        print(f'THE GREATEST COMMON DIVISOR IN {num1} AND {num2} IS {check}')
    else:
        print(f'THE TWO NUMBERS HAVE NO COMMON FACTORS. SO THE GREATEST COMMON DIVISOR IS 1')
'''

#PRINT ALL NUMBERS FROM 1 TO N EXCEPT 5
'''
print('HI THERE!')
num = int(input('ENTER THE NUMBER UPTO WHICH IS REQUIRED: '))
numbers = []

for b in range(1,num+1):
    numbers.append(b)

numbers.remove(5)

print(f'ALL THE NUMBERS FROM 1 TO {num} ARE {numbers}')
'''

#LEAP YEAR OR NOT
'''
print('HI THERE!')
year = int(input('ENTER THE YEAR TO BE CHECKED: '))

if year<1:
    print('ENTER A YEAR GREATER THAN 0')
elif year%100 == 0:
    if year%400 == 0:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year but centurial')
else:
    if year%4 == 0:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is a not leap year')
'''

#PRINT WHETHER THE GIVEN CHARACTER IS UPPER OR LOWER CASE OR NUMBERS OR SPECIAL CHARACTERS
'''
print('HI THERE!')
c = input('ENTER ANY CHARACTER: ')

if c>='0' and c<='9':
    print(f'{c} is a numberic character')
elif c>='A' and c<='Z':
    print(f'{c} is a upper case character')
elif c>='a' and c<='z':
    print(f'{c} is a lower case character')
else:
    print(f'{c} is a special character')
'''

#BREAK
'''
print('HI THERE!')
num1 = int(input('ENTER THE STARTING NUMBER: '))
num2 = int(input('ENTER THE ENDING NUMBER: ')) 

for i in range(num1,num2+1):
    for n in range(2,i):
        if i%n == 0:
            break
    else:
        print(i)
'''

#PASS
'''
print('HI THERE!')
num1 = int(input('ENTER THE STARTING NUMBER: '))
num2 = int(input('ENTER THE ENDING NUMBER: '))
avg = (num1+num2)/2

for b in range(num1,num2+1):
    if b == avg:
        continue
    else:
        print(b)
'''

#FIND SUM OF THE NUMBERS GIVEN BY USER
'''
print('HI THERE!')
random = 1
#total = []
store = 0

while random == 1:
    num = float(input('ENTER A NUMBER: '))
    if num == 4:
        print(f'THE SUM OF THE NUMBERS IS {store}')
        break
    else:
        store += num
        #total.append(num)
    ques = input('DO YOU WANT TO ADD ANOTHER NUMBER? ENTER EITHER yes or no: ')
    if ques == 'no':
        print(f'THE SUM OF THE NUMBERS IS {store}')
        break
    else:
        continue
'''

#SERIES
'''
print('HI THERE!')
power = int(input('ENTER THE NUMBER UP TO WHICH IS REQUIRED: '))
base = 2

for i in range(0,power+1):
    num = base**i
    print(num) 
'''

#PRINT SUM OF FIRST 'N' EVEN NUMBER
'''
print('HI THERE!')
n = int(input('HOW MANY EVEN NUMBERS DO YOU WANT TO FIND THE SUM OF: '))
final = n*2
sum = 0

for a in range(2,final+1,2):
    sum = sum + a

print('THEREFORE, THE SUM OF FIRST {0} EVEN NUMBERS IS {1}'.format(n, sum))
'''


        





















